import os

app_path = os.path.dirname(__file__) + "/"

# Logger Paths
root_path_log = app_path + "app_logs/"
root_path_logs = root_path_log + "logs.log"
root_path_global_logs = root_path_log + "global.log"
root_path_cleanup_logs = root_path_log + "cleanup.log"