import os
import sys

#TO USE:
#Option 1: Edit the options variable to contain each flag you would like to pass into piper-
#Option 2: In the command line, type: python single_atlas_project_init.py flag1 flag2 flag3 etc.
#If no names are provided in option 2 it will default to performing option 1
from datetime import datetime

options = ['--rec RECEPTOR.pdb',
           '--lig LIGAND.pdb',
           '--np 22',
           '--output-dir /0UTPUT/', #The keyword 0UTPUT will become replaced with the correct path when handled by the project_init script!
           ]

def run_piper(options):
    os.system('PIPER_PATH'+options)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        options = sys.argv[1:]
    options = ' '.join(options)
    run_piper(options)



# Options:
#
# Proteins
# --rec REC
#     Receptor file in PDB format
#
# --rec-list REC_LIST
#     List of receptor files, each line has one pdb file and optionally a list of chains
#
# --rec-chains [REC_CHAIN [REC_CHAIN …]]
#     Receptor chains whitespace separated, e.g. A B (default: all chains)
#
# --rec-mask REC_MASK
#     Receptor mask file in PDB format
#
# --rec-attraction [REC_ATTRACTION [REC_ATTRACTION …]]
#     Receptor residues in chain-residue format (e.g. A-123 B-125)
#
# --lig LIG
#     Ligand file in PDB format
#
# --lig-list LIG_LIST
#     List of ligand files, each line has one pdb file and optionally a list of chains
#
# --lig-chains [LIG_CHAIN [LIG_CHAIN …]]
#     Ligand chains whitespace separated, e.g. A B (default: all chains)
#
# --lig-mask LIG_MASK
#     Ligand mask file in PDB format
#
# --lig-attraction [LIG_ATTRACTION [LIG_ATTRACTION …]]
#     Ligand residues in chain-residue format (e.g. A-123)
#
# --restraint-set RESTRAINT_SET
#     Restraints in JSON-based format
#
# --vdw-het VDW_HET [VDW_HET …]
#     HETATM residue name to include in docking as vDw spheres (e.g. FAD), better results will occur if this residue is on the receptor side
#
# --add-het ADD_HET [ADD_HET …]
#     HETATM residue name and parameter file in format RESIDUE_NAME:PRM_FILE
#
#
# Docking Mode
# Default mode is enzyme-inhibitor mode
#
# --antibody
#     Run in antibody mode (Receptor is antibody, Ligand is antigen)
#
# --others
#     Run in “others” mode (based on ZDOCK Benchmark)
#
# --dimer
#     Run in dimer mode, receptor is treated as both units
#
# --trimer
#     Run in trimer mode, receptor is treated as all units
#
# --heparin
#     Run heparin docking, special heparin is used as ligand
#
# --nrots NROTS
#     Specify number of rotations (Default:70000, range: 1-70000, in dimer or trimer mode: Default:9994, range: 1-9994)
#
# --dont-minimize
#     Do not minimize the output models
#
# --coeffs-file COEFFS_FILE
#     Custom coefficients file (incompatible with others mode)
#
#
# Piper Location
# --piper--base BASE
#     Base directory for Piper installation
#
# --piper--license PIPER_LICENSE
#     Piper license file
#
#
# Multiprocessing
#
# --np NP
#     Use NP cores for docking (default: all)
#
# --mpi
#     Use MPI for docking across multiple machines; requires use of --np, --hostfile, or --host (default: use only cores on this machine)
#
# --hostfile HOSTFILE
#     MPI hostfile
#
# --host HOST
#     MPI hosts
#
# --custom-mpirun CUSTOM_MPIRUN
#     Custom mpirun script
#
#
# Other
# --output-dir OUTPUT_DIR
#     Specify directory for outputting results (default: current directory)
#
# --prefix PREFIX
#     Specify prefix for output complexes (default: model)
#
# --sorted-dirs
#     Create size_sorted and energy_sorted directories for multi-docking
#
# --advanced ADVANCED
#     Advanced parameters in json format
