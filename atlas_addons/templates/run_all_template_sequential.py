import os
subfolder_run_files = SUBPROCESS_LIST
for cmd in subfolder_run_files:
    os.system('python '+cmd)
