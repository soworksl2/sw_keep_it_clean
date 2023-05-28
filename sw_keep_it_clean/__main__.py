import os
import json

from clean_instructions import CleanInstruction
from normal_cleaner import NormalCleaner
from util.error_handling import exit_with_error


LOCALAPPDATA_PATH = os.environ['LOCALAPPDATA']
SW_TOOLS_PATH = os.path.join(LOCALAPPDATA_PATH, 'sw_tools')
CONFIGURATION_PATH = os.path.join(SW_TOOLS_PATH, 'keep_it_clean_configuration.json')


if not os.path.isfile(CONFIGURATION_PATH):
    exit_with_error(f'cannot read the configuration file at path "{CONFIGURATION_PATH}"')

with open(CONFIGURATION_PATH, 'r') as f:
    configuration_json_ditc = json.load(f)

clean_instructions = CleanInstruction.from_json_dict(configuration_json_ditc)

NormalCleaner = NormalCleaner(clean_instructions)

NormalCleaner.execute()
