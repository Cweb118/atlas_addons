import sys
import os

#TO USE:
#Option 1: Edit the project_names variable to contain each name you would like to create a project folder for
#Option 2: In the command line, type: python single_atlas_project_init.py name1 name2 name3 etc.
#If no names are provided in option 2 it will default to performing option 1

project_names = ['1ubq']


def init_project_files(project_name):
    print("Creating atlas- project folder for "+project_name+"...")
    main_path = '../atlas_projects/'
    print(main_path)
    project_folder = main_path+project_name+"/"
    project_output = project_folder+project_name+"_output/"

    paths = [main_path, project_folder, project_output]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

    run_template = open('templates/run_template_atlas.py', "r")
    run_template_txt = run_template.read()
    run_txt = run_template_txt.replace('0UTPUT', project_name+"_output")
    run_txt = run_txt.replace('ATLAS_PATH', '../../atlas_package/bin/run_atlas ')

    project_run = open(project_folder+'run_'+project_name+'_atlas.py', "w")
    project_run.write(run_txt)

    run_template.close()
    project_run.close()

    print(project_name+" creation complete!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_names = sys.argv[1:]
    for project_name in project_names:
        init_project_files(project_name)
