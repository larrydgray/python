from configparser import ConfigParser

config = ConfigParser()
config['main_section'] = {
    'key1': 'value1',
    'key2': 123,
    'key3': 123.45,
}

with open('config.ini', 'w') as output_file:
    config.write(output_file)

# Example output in `congig.ini`:
"""
[main_section]
key1 = value1
key2 = 123
key3 = 123.45
"""
