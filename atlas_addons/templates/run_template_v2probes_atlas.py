import os
import shutil
import sys

#TO USE:
#Option 1: Edit the options variable to contain each flag you would like to pass into piper-
#Option 2: In the command line, type: python project_init_single_atlas.py flag1 flag2 flag3 etc.
#If no names are provided in option 2 it will default to performing option 1

options = ['RECEPTOR.pdb',
           '--np 14',
           '--v2-probes',
           ]

# WARNING: If you have this turned on it will take the first pdb it finds in the folder and run atlas on it.
# Only enable this if you are sure you will not have multiple pdbs in the same folder.
auto_detect_pdb = False
# If enabled, this will run atlas_classify_druggability after the main atlas script
check_drug = True

def run_atlas(options):
    os.system('ATLAS_PATH/run_atlas '+options)


def check_druggability(output_folder):
    files = os.listdir(output_folder)
    tar = [x for x in files if 'tar.xz' in x][0]
    output_filename = output_folder+"atlas_classify_druggabilty_v2_"+tar.split('.')[0]+".txt"
    os.system("ATLAS_PATH/atlas_classify_druggability "+tar+"  > "+output_filename)


if __name__ == "__main__":
    filedir = os.path.dirname(__file__)
    files = os.listdir(filedir)
    output_folder = [k for k in files if 'v2_output' in k][0]
    if len(sys.argv) > 1:
        options = sys.argv[1:]
    if auto_detect_pdb:
        files = os.listdir(filedir)
        pdb_name = [x for x in files if '.pdb' in x][0]
        options = [pdb_name]+options[1:]
    else:
        pdb_name = options[0]
    options = [filedir+'/'+output_folder+'/'+options[0]]+options[1:]
    options = ' '.join(options)
    shutil.copy(filedir+'/'+pdb_name, filedir+'/'+output_folder+'/'+pdb_name)
    run_atlas(options)
    if check_drug:
        check_druggability(filedir+'/'+output_folder+'/')


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

