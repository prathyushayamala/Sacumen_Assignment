from src.Modules.readmodule import ReadModule
import os

def test_convert_yaml_file():
    expected_output = {'languages:': {'  pascal': 'Lame', '  python': 'Elite', '  perl': 'Elite'}, 'foods:': ['Mango', 'Strawberry', 'Orange', 'Apple'], 'employed': 'True', 'skill': 'Elite', 'job': 'Developer', 'name': "Martin D'vloper"}
    assert ReadModule().read_file(os.getcwd()+'\\test\\test.yaml') == expected_output

def test_convert_conf_file():
    expected_output = {'section1': {'database': 'database1', 'server': 'server2', 'host': 'host2', 'port': '798'}, 'cfs-lib': {'server': 'server1', 'host': 'host1', 'port': '6776'}}
    assert ReadModule().read_file(os.getcwd()+'\\test\\test.conf') == expected_output

def test_convert_cfg_file():
    expected_output = {'section1': {'database': 'database1', 'server': 'server2', 'host': 'host2', 'port': '798'}, 'cfs-lib': {'server': 'server1', 'host': 'host1', 'port': '6776'}}
    assert ReadModule().read_file(os.getcwd()+'\\test\\test.cfg') == expected_output

def test_convert_ini_file():
    expected_output = {'mypy': {'warn_no_return': 'True', 'strict_optional': 'True', 'disallow_untyped_calls': 'True', 'disallow_untyped_defs': 'True', 'disallow_subclassing_any': 'True', 'disallow_any_generics': 'True', 'disallow_any_expr': 'True', 'disallow_any_decorated': 'True'}}
    assert ReadModule().read_file(os.getcwd()+'\\test\\test.ini') == expected_output

def test_convert_text_file():
    expected_output = {}
    assert ReadModule().read_file(os.getcwd()+'\\test\\test.txt') == expected_output