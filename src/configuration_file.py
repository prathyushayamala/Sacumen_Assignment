"""
This file is used to call the relatable modules based on the user's input given
"""
from Modules.readmodule import ReadModule
from Modules.writemodule import WriteModule
import re
import os

class Configuration_File:
    def read_config_file(self):
        """
        This method is used to take input from user
        and call the readmodule or writemodule based on the file given.
        If given file name is not valid, It will print a basic message for the same
        """
        file_name = input('Enter the file name')
        if re.search('[yaml|conf|ini|cfg]$', file_name):
            ReadModule().read_file(file_name)
        elif re.search("[txt]$", file_name):
            WriteModule().read_configurations_file(file_name)
        else:
            print("Invalid File Name")
            return {}