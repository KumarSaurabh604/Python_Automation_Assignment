import configparser


def GetDataFromFile(section, option):
    # Load configuration from properties file
    config = configparser.RawConfigParser()
    config_file_path = 'config.properties'
    config.read(config_file_path)

    # Fetching the username value
    elementName = config.get(section, option)
    print(f"Username fetched from config: {elementName}")
    return elementName


def SetDataInFile(section, key, value):
    # Load the configuration from the properties file
    config = configparser.RawConfigParser()
    config_file_path = 'config.properties'
    config.read(config_file_path)

    # Check if the section exists, if not, add it
    if not config.has_section(section):
        config.add_section(section)

    # Set the new key-value pair in the specified section
    config.set(section, key, value)

    # Write the changes back to the properties file
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

    print(f"Set {key} in {section} to {value} in {config_file_path}")
