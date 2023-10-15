import os
from Flask_App.paths import root_path_log

if not os.path.exists(root_path_log):
    os.makedirs(root_path_log)