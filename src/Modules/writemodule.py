"""
This module is used to generate the config file based on the requirements 
in the file name given as input
"""
from configparser import ConfigParser

class WriteModule:
    def __init__(self):
        self.config = ConfigParser()

    def read_configurations_file(self,file_name):
        """
        Used to read the file and generates the config file
        Params:
            file_name : Name of the file : str
        """
        try:
            file_pointer = open(file_name,'r')
            file_contents = file_pointer.readlines()

            self.set_configurations(file_contents)
            file_name = self.generate_config_file()
            return file_name
        except:
            return {}

    def set_configurations(self,file_contents):
        """
        Used to extract the configurations from the file name given
        Params:
            file_contents : List of the configurations present in the file : list
        """
        section = 'cfs-lib'
        configuration_key = ''
        configuration_value = ''
        for line in file_contents:
            line = line.replace('\n','').split(' ')
            for word in line:
                if word == 'Under':
                    section = line[line.index(word)+1]
                elif word == 'Set':
                    configuration_key = line[line.index(word)+1]
                    configuration_value = line[line.index(word)+3]
                    break
            if self.config.has_section(section):
                self.config[section][configuration_key] = configuration_value
            else:
                self.config.add_section(section)
                if configuration_key!='' and configuration_value != '':
                    self.config[section][configuration_key] = configuration_value
                else:
                    pass

    def generate_config_file(self):
        """
        Generates the config file using the configurations extracted from the file given
        """
        with open(os.getcwd()+'\\src\\config_files\\config.ini','w') as config_file:
            self.config.write(config_file)
        return 'config.ini'