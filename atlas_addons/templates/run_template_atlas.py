import os
import shutil
import sys
from datetime import datetime
from subprocess import Popen, PIPE
#===============
#
# File: run_template_atlas.py
# Version: 1.0, 08-22-22
# Usage (cmd): python <filename>
# Description: Runs atlas for the designated pdb (which can be auto-detected)
#
# Authors: Caleb Weber, Oleksandr Savytskyi, Ph.D, Thomas Caulfield, Ph.D
# CAULFIELD LABORATORY, PROPERTY OF MAYO CLINIC
# https://www.mayo.edu/research/labs/drug-discovery-design-optimization-novel-therapeutics-therapeutics
#
#===============

options = ['RECEPTOR.pdb',
           '--np 22',
           ]

# WARNING: If you have this turned on it will take the first pdb it finds in the folder and run atlas on it.
# Only enable this if you are sure you will not have multiple pdbs in the same folder.
auto_detect_pdb = True
# If enabled, this will run atlas_classify_druggability after the main atlas script
check_drug = True

def run_atlas(options):
    cmd = 'ATLAS_PATH'+options
    log_name = __file__.replace('.py', '_log.txt')
    starttime = datetime.now()
    logtxt = "Start Time: "+str(starttime)+'\n'
    logfile = open(log_name, "w")

    proc = Popen(
        "python "+cmd,
        shell=True,
        stdout=PIPE,
        stderr=PIPE)
    stdout, stderr = proc.communicate()
    msg = f'[{cmd!r} exited with {proc.returncode}]'
    print(msg)
    logtxt += msg+'\n'
    if stdout:
        msg = f'[stdout]\n{stdout.decode()}'
        print(msg)
        logtxt += msg+'\n'
    if stderr:
        msg = f'[stderr]\n{stderr.decode()}'
        print(msg)
        logtxt += msg+'\n'
    endtime = datetime.now()
    logtxt += "End Time: "+str(endtime)+'\n'

    endtime = datetime.now()
    duration = endtime - starttime
    duration_in_s = duration.total_seconds()
    days = divmod(duration_in_s, 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    seconds = divmod(minutes[1], 1)
    print("Run Duration: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))
    logtxt += "Run Duration: "+str(days[0])+" days, "+str(hours[0])+" hours, "+str(minutes[0])+" minutes, "+str(seconds[0])+" seconds"

    logfile.write(logtxt)
    logfile.close()



def check_druggability():
    files = os.listdir()
    tar = [x for x in files if 'tar.xz' in x][0]
    output_filename = "atlas_classify_druggabilty_"+tar.split('.')[0]+".txt"
    os.system("ATLAS_PATH/atlas_classify_druggability "+tar+"  > "+output_filename)


if __name__ == "__main__":
    files = os.listdir()
    output_folder = [k for k in files if 'output' in k][0]
    if len(sys.argv) > 1:
        options = sys.argv[1:]
    if auto_detect_pdb:
        files = os.listdir()
        pdb_name = [x for x in files if '.pdb' in x][0]
        options = [pdb_name]+options[1:]
    else:
        pdb_name = options[0]
    options = [output_folder+'/'+options[0]]+options[1:]
    options = ' '.join(options)
    shutil.copy(pdb_name, output_folder+'/'+pdb_name)
    run_atlas(options)
    shutil.move(output_folder+'/'+pdb_name, pdb_name)
    if check_drug:
        check_druggability()






# Options
#
# --prefix PREFIX
#     Prefix results with given prefix, otherwise results will be prefixed based on input filename e.g. 1acb.pdb -> 1acb_atlas_ .
#
# --np N
#     Limit use of mapping to using N cores.
#
# --box-pdb PDB
#     Define a box for mapping using a pdb file.
#
# --box-residue RESIDUE
#     Define a box using a residue present in the protein.
#
# --box-pad PADDING
#     Padding around a box used to be used for mapping.
#
# --ppi
#     Run in a special mode that favors protein-protein interaction sites by reducing the cavity terms that favor more traditional drug sites.
#
# --hydrogen-bonding
#     Use hydrogen bonding function for minimization
#
# --hb-filter
#     Filter out polar probes that do not form hydrogen bonds
#
# --v2-probes
#     Use V2 probe set (fake ligands)
#
# --probes PROBES
#     Custom set of probes
#
# --auto-flex
#     Automatically choose consensus sites to be used for flexibility based on predicted binding site rather than manually choosing sites (see Flexibility section below).
#
# --atlas--base
#     If the atlas- scripts are run from within their directory, all necessary parameter files and dependencies should automatically be found. If you move the scripts, you can use this option to specify the location of these files.
#
# --atlas--license
#     By default, your atlas- license will be found within the atlas- installation. If, for some unexpected reason, this file is located elsewhere, you may use this option to specify its location.
#

