import os
import json


class program:
    @staticmethod
    def load_configs():
        app_full_path = os.path.realpath(__file__)
        application_path = os.path.dirname(app_full_path)
        filename = os.path.join(application_path, 'Static/appsettings.json')
        
        with open(filename) as json_file:
            return json.load(json_file)
