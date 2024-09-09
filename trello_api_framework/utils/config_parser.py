import configparser
import os


class ConfigParser:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_file_path = os.path.join(os.path.dirname(__file__),
                                        '../config/config.ini')  # Adjust the path accordingly
        self.config.read(self.config_file_path)

    def get_trello_config(self):
        return {
            'api_key': self.config.get('trello', 'api_key'),
            'token': self.config.get('trello', 'token'),
            'base_url': self.config.get('trello', 'base_url'),
            'card_id': self.config.get('trello', 'card_id'),
            'invalid_card_id': self.config.get('trello', 'invalid_card_id'),
            'id_list': self.config.get('trello', 'id_list'),
            'invalid_id_list': self.config.get('trello', 'invalid_id_list')
        }

    def set_trello_config(self, key, value):
        # Check if the section 'trello' exists, if not, add it
        if not self.config.has_section('trello'):
            self.config.add_section('trello')

        # Set the key and value
        self.config.set('trello', key, value)

        # Write the changes back to the config.ini file
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)
        print(f"Updated {key} in 'trello' section with value {value}")