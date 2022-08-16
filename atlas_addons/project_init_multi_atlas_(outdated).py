import sys
import os

# TO USE:
# Edit the project_folders variable, where:
#   - the name to the left of the colon is the project folder
#   - the list of names to the right of the colon are sub folders for running variations of the same project in sequence
# Edit the project_templates variable, where:
#   - the name to the left of the colon is the name of a sub folder
#   - the name to the right of the colon is the name of the template you would like put in that folder


project_folders = {
    '1ubq':['1ubq-1', '1ubq-2']
}

project_templates = {
    '1ubq-1':'run_template_atlas.py',
    '1ubq-2':'run_template_atlas.py'
}

def init_project_files(project_name):
    print("Creating atlas- project folder for "+project_name+"...")
    main_path = '../atlas_projects/'
    print(main_path)
    project_folder = main_path+project_name+"/"
    paths = [main_path, project_folder]
    subfolder_names = project_folders[project_name]
    for subfolder_name in subfolder_names:
        subfolder = project_folder+subfolder_name+"/"
        subfolder_output = subfolder+subfolder_name+"_output/"
        paths.append(subfolder)
        paths.append(subfolder_output)

    print(paths)
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
    subfolder_run_files = []
    for subfolder_name in subfolder_names:
        subfolder_template = project_templates[subfolder_name]
        run_template = open(subfolder_template, "r")
        run_template_txt = run_template.read()
        run_txt = run_template_txt.replace('0UTPUT', subfolder_name+"_output")
        run_txt = run_txt.replace('ATLAS_PATH', '../../../atlas_package/bin/run_atlas ')

        subfolder_path = project_folder+subfolder_name+"/"
        subfolder_run_file = subfolder_path+'run_'+subfolder_name+'_atlas.py'
        subproject_run = open(subfolder_run_file, "w")
        subproject_run.write(run_txt)
        subfolder_run_files.append(subfolder_run_file)

        run_template.close()
        subproject_run.close()


    run_all_txt = "import os\n\n" \
                  "subfolder_run_files = "+str(subfolder_run_files)+"\n" \
                  "for path in subfolder_run_files:\n\t" \
                        "split = path.split('/')\n\t" \
                        "os.chdir(split[-2])\n\t" \
                        "os.system('python '+split[-1])\n\t" \
                        "os.chdir('../')"
    project_run = open(project_folder+project_name+'_run_all.py', "w")
    project_run.write(run_all_txt)
    project_run.close()


    print(project_name+" creation complete!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_names = sys.argv[1:]
    for project_name in project_folders.keys():
        init_project_files(project_name)
