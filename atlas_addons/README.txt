#===============
#
# Authors: Caleb Weber, Oleksandr Savytskyi, Ph.D, Thomas Caulfield, Ph.D
# CAULFIELD LABORATORY, PROPERTY OF MAYO CLINIC
# https://www.mayo.edu/research/labs/drug-discovery-design-optimization-novel-therapeutics-therapeutics
#
#===============

Within this folder are the following:

- project_init scripts:
    When run, these scripts will create project folders which will contain customized template scripts which will run atlas
    To set these up, you simply edit fields for names
    For projects that set up run files for multiple pdbs, you can place all pdbs in the pdb_input folder and they will auto generate

- templates folder:
    Within this folder are multiple templates for running atlas
    Each file could be manually set up by inputting pdb titles and the path to atlas
    Alternatively, if a project_init script is run, these templates will be copied and customized, and moved into a folder
    There are also run_all scripts. These are designed to be copied by a project_init script so that a user can run the customized copy in the project folder, which will trigger all individual run scripts in that project.

Use Guide:

1. Select which kind of project_init script you would like to run (multi if using more than one pdb or running more than one time on one pdb)
2. Designate in this script the name of the project and which run template(s) you would like to use
    Note: You will not have to edit the run templates with details of your project, but if there are none with your desired parameters then you may edit or make a new one
    If your script supports multiple runs (multi), place the pdbs you would like to analyze in the pdb_input folder and designate the processing style (sequential, parallel, or pairwise).
3. Run the command: python <project_init_script>.py
4. Navigate to the newly created project folder. Confirm that there is a run_all file and a folder for each pdb (if multi)
    Note: Each pdb folder will contain the pdb and a run file accompanied by an output folder based on each template you have designated
5. Run the command: python <run_all_project_script>.py
6. After the run: Verify output folders contain correct information. Logs can be found in the pdb's folder.
