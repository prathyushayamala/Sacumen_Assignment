"""
This module is used to read the configurations from the various configurations files
and generates the flat dictionaries for the same
"""
from Modules.file_type_mappings import FILE_TYPE_MAPPINGS

class ReadModule:
    def read_file(self,file_name):
        """
        Used to read the configuration file 
        params : 
            file_name : Name of the file : str
        Returns flattened dictionary
        """
        fp = open(file_name,'r')
        file_content = fp.readlines()
        file_content.reverse()
        file_type = file_name.split('.')[-1]
        return self.get_config_file(file_content,file_type)


    def get_config_file(self,file_content,file_type):
        """
        Used to read the configurations and creates a dictionary for the same
        Params:
            file_content : List of configurations from the config files : list
            file_type : Type of the file(yaml/conf/cfg) : str
        Returns Configuration Dictionary
        """
        config_dict = {}
        sub_dict = {}
        list_of_values = []
        for line in file_content:
            if not (line.startswith('#') or line.startswith('\n') or line.startswith('---') or line.startswith('...')):
                configuration = line.replace('\n','').split(FILE_TYPE_MAPPINGS[file_type])
                if len(configuration) > 1:
                    if configuration[0] in sub_dict:
                        sub_dict[configuration[0]].append(configuration[1])
                    else:
                        sub_dict[configuration[0]] = configuration[1]
                elif len(configuration) == 1:
                    if configuration[0].startswith('  - '):
                        list_of_values.append(configuration[0].replace('  - ','').strip())
                    elif list_of_values != []:
                        sub_dict[configuration[0]] = list_of_values
                        list_of_values = []
                    else:
                        configuration = configuration[0].replace('[','').replace(']','').strip()
                        config_dict[configuration] = sub_dict
                        sub_dict = {}
                else:
                    pass
        if sub_dict != {}:
            config_dict.update(sub_dict)
        print(config_dict)
        return config_dict
