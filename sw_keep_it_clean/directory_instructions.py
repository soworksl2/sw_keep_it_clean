from dataclasses import dataclass

from error_handling import exit_with_error

ABS_PATH_KEY = 'abs_path'
EXCLUSION_ITEMS_KEY = 'exclusion_items'
LIFE_TIME_KEY = 'life_time'

@dataclass
class DirectoryInstructions:
    abs_path: str
    exclusion_items: list[str]
    life_time: int

    @staticmethod
    def from_json_dict(json_dict: dict) -> "DirectoryInstructions":
        abs_path = json_dict[ABS_PATH_KEY]
        exclusion_items = json_dict.get(EXCLUSION_ITEMS_KEY, [])
        life_time = json_dict.get(LIFE_TIME_KEY, 30)

        if not isinstance(exclusion_items, list):
            exit_with_error(f'the {EXCLUSION_ITEMS_KEY} field is not a list')

        if not isinstance(life_time, int):
            exit_with_error(f'the {LIFE_TIME_KEY} field is not an integer')
        
        return DirectoryInstructions(abs_path, exclusion_items, life_time)
