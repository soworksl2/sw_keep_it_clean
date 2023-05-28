import os

from clean_instructions import CleanInstruction
from normal_cleaner import NormalCleaner


LOCALAPPDATA_PATH = os.environ['LOCALAPPDATA']
SW_TOOLS_PATH = os.path.join(LOCALAPPDATA_PATH, 'sw_tools')
CONFIGURATION_PATH = os.path.join(SW_TOOLS_PATH, 'keep_it_clean_configuration.json')


clean_instructions = CleanInstruction.from_json_file(CONFIGURATION_PATH)

NormalCleaner = NormalCleaner(clean_instructions)

NormalCleaner.execute()
