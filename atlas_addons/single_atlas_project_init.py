import sys
import os

#===============
#
# File: single_atlas_project_init.py
# Version: 1.0, 08-22-22
# Usage (cmd): python single_atlas_project_init.py
# Description: Creates a project folder for the given project name, then installs the designated run template within
#
# Authors: Caleb Weber, Oleksandr Savytskyi, Ph.D, Thomas Caulfield, Ph.D
# CAULFIELD LABORATORY, PROPERTY OF MAYO CLINIC
# https://www.mayo.edu/research/labs/drug-discovery-design-optimization-novel-therapeutics-therapeutics
#
#===============



# Change your project's name here
project_name = '1ubq'
# Designate which template you wish to use (from the templates folder) here
run_template = 'run_template_atlas.py'

#Following project creation, place your pdb into the newly created folder.

def init_project_files(project_name, run_template):
    print("Creating atlas- project folder for "+project_name+"...")
    main_path = '../atlas_projects/'
    print(main_path)
    project_folder = main_path+project_name+"/"
    project_output = project_folder+project_name+"_output/"

    paths = [main_path, project_folder, project_output]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

    run_template = open('templates/'+run_template, "r")
    run_template_txt = run_template.read()
    run_txt = run_template_txt.replace('0UTPUT', project_name+"_output")
    run_txt = run_txt.replace('ATLAS_PATH', '../../../atlas_package/bin/run_atlas ')

    project_run = open(project_folder+'run_'+project_name+'_atlas.py', "w")
    project_run.write(run_txt)

    run_template.close()
    project_run.close()

    print(project_name+" creation complete!")


if __name__ == "__main__":
    init_project_files(project_name, run_template)




