import logging

from Flask_App.Classes.Cleanup_Class import Cleanup_Class
from Flask_App.Classes.File_Handler import File_Content_Streamer_Thread

from Flask_App.paths import root_path_cleanup_logs


maxBytes = 64*1024


# Cleanup Thread
cleanup_thread = Cleanup_Class(
    name="Cleanup Thread",
    logger=None,
    logger_level_stdo=logging.DEBUG,
    logger_level_file=logging.DEBUG,
    logger_file_path=root_path_cleanup_logs,
    mode="a", 
    maxBytes=maxBytes, 
    backupCount=2
)
cleanup_thread.start_Thread()

cleanup_logger_streamer = File_Content_Streamer_Thread(
    path=root_path_cleanup_logs,
    # wait_thread=log_collection_thread,
    is_yield=True
)


