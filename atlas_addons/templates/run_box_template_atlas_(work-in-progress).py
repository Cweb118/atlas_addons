import os
import shutil
import sys

#TO USE:
#Option 1: Edit the options variable to contain each flag you would like to pass into piper-
#Option 2: In the command line, type: python project_init_single_atlas.py flag1 flag2 flag3 etc.
#If no names are provided in option 2 it will default to performing option 1

options = ['RECEPTOR.pdb',
           '--np 22',
           ]

# WARNING: If you have this turned on it will take the first pdb it finds in the folder and run atlas on it.
# Only enable this if you are sure you will not have multiple pdbs in the same folder.
auto_detect_pdb = True

# As an exception, this can be put in the same folder as the pdb so long as 'box' is somewhere in the filename
# This will allow it to be detected and moved to its own folder before the pdb is determined
auto_detect_box = True

def run_atlas(options):
    os.system('ATLAS_PATH'+options)

if __name__ == "__main__":
    files = os.listdir()
    output = [k for k in files if 'output' in k][0]
    if len(sys.argv) > 1:
        options = sys.argv[1:]

    if auto_detect_box:
        box = [x for x in files if 'box' in x][0]
        #TODO: Replace box term in options
    else:
        #TODO: Get box from options
        pass
    box_folder = '/'+output.split('_')[0]+'_box/'
    if not os.path.exists(box_folder):
        os.makedirs(box_folder)
    shutil.move(box, box_folder+'/'+box)

    if auto_detect_pdb:
        pdb_name = [x for x in files if '.pdb' in x][0]
        options = [pdb_name]+options[1:]
    else:
        pdb_name = options[0]
    options = ' '.join(options)
    run_atlas(options)
    files = os.listdir()
    for file in files:
        if file != output:
            if file != pdb_name:
                if file != os.path.basename(__file__):
                    shutil.move(file, output+'/'+file)


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

