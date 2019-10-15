from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


# Get a list of all sections
print('Sections: %s' % config.sections())

# You can treat it as an iterable and check for keys
# or iterate through them
if 'main_section' in config:
    print('Main section does exist in config.')

for section in config:
    print('Section: %s' % section)
    for key, value in config[section].items():
        print('Key: %s, Value: %s' % (key, value))

# If you know exactly what key you are looking for,
# try to grab it directly, optionally providing a default
print(config['main_section'].get('key1'))  # Gets as string
print(config['main_section'].getint('key2',))
print(config['main_section'].getfloat('key3'))
print(config['main_section'].getboolean('key99', False))
