import json
import os


SETTINGS_FILE = "config/company_settings.json"


def load_settings(default_settings):

    if os.path.exists(SETTINGS_FILE):

        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)

    return default_settings



def save_settings(settings):

    with open(SETTINGS_FILE, "w") as file:

        json.dump(
            settings,
            file,
            indent=4
        )



def get_company_settings():

    from config.company_profile import COMPANY_PROFILE

    return load_settings(
        COMPANY_PROFILE
    )