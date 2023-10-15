

 
import time

from Flask_App.Classes.Task_Handler import Task_Handler_Class



class Cleanup_Class(Task_Handler_Class):
    def __init__(self, *args, **kwargs):
        super(Cleanup_Class, self).__init__(*args, **kwargs)
        
        self.__parameters_template = {
            "param1": ""
        }
        self.parameters = self.__parameters_template.copy()


    def set_Parameters(self, param1: str) -> int:
        self.parameters = self.__parameters_template.copy()
        
        self.parameters["param1"] = param1
        return 0
   

    def task(self, param1):
        self.logger.info(f"Starting with parameters; {param1}")
        try:
            # Check Thread State
            time.sleep(1)
            if self.is_Thread_Stopped():
                return -1
                    
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
        
        self.logger.info(f"Task Finished!")
        
        return 0