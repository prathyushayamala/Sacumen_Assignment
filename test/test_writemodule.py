from src.Modules.writemodule import WriteModule
import os

def test_create_config_file():
    filename = WriteModule.read_configurations_file(os.getcwd()+'\\test\\configurations.txt')
    with open(filename,'r') as fp:
        file_content = fp.readlines()
    output_data = ["[Fruits]\n","fruit1 = Apple\n","fruit2 = Banana\n","[Vegetables]\n","vegetable1 = Onion\n"]
    assert file_content == output_data

def test_create_empty_config_file():
    filename = WriteModule.read_configurations_file(os.getcwd()+'\\test\\configurations_test_file.txt')
    with open(filename,'r') as fp:
        file_content = fp.readlines()
    output_data = ['cfs-lib']
    assert file_content == output_data