from dataclasses import dataclass

from util.error_handling import exit_with_error
from directory_instructions import DirectoryInstructions


DIRECTORIES_INSTRUCTIONS_KEY = 'directories_instrucions'

@dataclass
class CleanInstruction:
    directories_instrucions: list[DirectoryInstructions]

    @staticmethod
    def from_json_dict(json_dict: dict) -> "CleanInstruction":
        try:
            json_directories_instructions = json_dict[DIRECTORIES_INSTRUCTIONS_KEY]
        except:
            exit_with_error(f'an error ocurred while reading the {DIRECTORIES_INSTRUCTIONS_KEY} field from the configuration file')

        if not isinstance(json_directories_instructions, list):
            exit_with_error(f'the {DIRECTORIES_INSTRUCTIONS_KEY} field in the configuration file expected a list')

        directories_instructions: list[DirectoryInstructions] = []

        for i, json_directory_instructions in enumerate(json_directories_instructions):
            if not isinstance(json_directory_instructions, dict):
                exit_with_error(f'the obj of index={i} in the {DIRECTORIES_INSTRUCTIONS_KEY} field was expected an obj')

            directories_instructions.append(DirectoryInstructions.from_json_dict(json_directory_instructions))

        return CleanInstruction(directories_instructions)
