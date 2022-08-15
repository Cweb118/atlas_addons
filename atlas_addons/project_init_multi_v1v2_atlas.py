import shutil
import sys
import os

# TO USE:
# Edit the project_folders variable, where:
#   - the name to the left of the colon is the project folder
#   - the list of names to the right of the colon are sub folders for running variations of the same project in sequence
# Edit the project_templates variable, where:
#   - the name to the left of the colon is the name of a sub folder
#   - the name to the right of the colon is the name of the template you would like put in that folder


main_project_folder_name = '1ubq'
v1_template = 'run_template_v1probes_atlas.py'
v2_template = 'run_template_v2probes_atlas.py'
templates = [v1_template, v2_template]


if __name__ == "__main__":
    print("Creating atlas- project folder for "+main_project_folder_name+"...")
    main_path = '../atlas_projects/'
    project_folder = main_path+main_project_folder_name+"/"
    paths = [main_path, project_folder]
    pdbs = os.listdir('pdb_input/')
    subfolder_names = [x.split('.')[0] for x in pdbs]
    for subfolder_name in subfolder_names:
        subfolder = project_folder+subfolder_name+"/"
        subfolder_v1_output = subfolder+subfolder_name+"_v1_output/"
        subfolder_v2_output = subfolder+subfolder_name+"_v2_output/"
        paths.append(subfolder)
        paths.append(subfolder_v1_output)
        paths.append(subfolder_v2_output)

    print(paths)
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
    subfolder_run_files = []
    for pdb in pdbs:
        subfolder_name = pdb.split('.')[0]
        subfolder_path = project_folder+subfolder_name+"/"
        shutil.move('pdb_input/'+pdb, subfolder_path+pdb)
        for template_name in templates:
            template = 'templates/'+template_name
            run_template = open(template, "r")
            run_template_txt = run_template.read()
            run_txt = run_template_txt.replace('RECEPTOR.pdb', pdb)
            run_txt = run_txt.replace('ATLAS_PATH', '../../atlas_package/bin')

            subfolder_template_name = template_name.replace('template', subfolder_name)
            subfolder_run_file = subfolder_path+subfolder_template_name
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
    project_run = open(project_folder+main_project_folder_name+'_run_all.py', "w")
    project_run.write(run_all_txt)
    project_run.close()

    print(main_project_folder_name+" creation complete!")


