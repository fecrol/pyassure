import os
import json

class PyAssureConfig:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(PyAssureConfig, cls).__new__(cls)
        
        return cls.__instance

    def __init__(self):
        self.__config_file_path = os.getcwd()
        self.__config_file_name = "pyassure.config.json"
        self.__full_config_file_path = f"{self.__config_file_path}/{self.__config_file_name}".replace("\\", "/")

        self.__pyassure_config_data = self.__read_config_file()

    def __read_config_file(self):
        try:
            file = open(self.__full_config_file_path)
            file_as_json = json.load(file)

            return file_as_json
        except Exception as err:
            print(err)
    
    def get_data(self):
        return self.__pyassure_config_data

pyassure_config = PyAssureConfig()
