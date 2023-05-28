import os
from dataclasses import dataclass
import json

from directory_instructions import DirectoryInstructions


@dataclass
class CleanInstruction:
    directories_instrucions: list[DirectoryInstructions]

    @staticmethod
    def from_json_file(path_to_json:str) -> "CleanInstruction":
        if not os.path.isfile(path_to_json):
            raise Exception(f'an error happens while read the configuration file at "{path_to_json}"')

        with open(path_to_json) as f:
            json_content = json.load(f)

        json_directories_instructions = json_content['directories_instructions']

        if not isinstance(json_directories_instructions, list):
            raise Exception('the configuration file has bad format')

        directories_instructions: list[DirectoryInstructions] = []

        for json_directory_instructions in json_directories_instructions:
            directories_instructions.append(DirectoryInstructions.from_json_dict(json_directory_instructions))

        return CleanInstruction(directories_instructions)
