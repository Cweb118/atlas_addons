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
probe_versions = ['v1', 'v2']
v1_template = 'run_template_atlas_probes_V1.py'
v2_template = 'run_template_atlas_probes_V2.py'
templates = [v1_template, v2_template]

#Choose from the following options:
# - sequential: runs each atlas simulation in order
# - pairwise: runs v1/v2 simulations in parallel, with the variable pdbs in sequence
# - parallel: runs all simulations at once
run_style = 'pairwise'

if __name__ == "__main__":
    print("Creating atlas- project folder for "+main_project_folder_name+"...")
    main_path = '../atlas_projects/'
    project_folder = main_path+main_project_folder_name+"/"
    paths = [main_path, project_folder]
    pdbs = os.listdir('pdb_input/')
    pdbs = [x for x in pdbs if '.pdb' in x]
    subfolder_names = [x.split('.')[0] for x in pdbs]
    for subfolder_name in subfolder_names:
        subfolder = project_folder+subfolder_name+"/"
        paths.append(subfolder)
        for probe_version in probe_versions:
            subfolder_vx_output = subfolder+subfolder_name+"_"+probe_version+"_output/"
            paths.append(subfolder_vx_output)

    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
    subfolder_run_files = []
    for pdb in pdbs:
        subfolder_name = pdb.split('.')[0]
        subfolder_path = project_folder+subfolder_name+"/"
        shutil.move('pdb_input/'+pdb, subfolder_path+pdb)
        pair = []
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
            subfolder_file_path = subfolder_run_file.split('/')[-2]+'/'+subfolder_run_file.split('/')[-1]
            pair.append(subfolder_file_path)

            run_template.close()
            subproject_run.close()

        if run_style == 'pairwise':
            subfolder_run_files.append(pair)
        else:
            for file in pair:
                subfolder_run_files.append(file)

    run_all_template_name = 'templates/template_run_all_'+run_style+'.py'
    run_all_template = open(run_all_template_name, "r")
    run_all_template_txt = run_all_template.read()
    run_all_txt = run_all_template_txt.replace('SUBPROCESS_LIST', str(subfolder_run_files))
    project_run = open(project_folder+main_project_folder_name+'_run_all_'+run_style+'.py', "w")
    project_run.write(run_all_txt)
    project_run.close()

    print(main_project_folder_name+" creation complete!")


