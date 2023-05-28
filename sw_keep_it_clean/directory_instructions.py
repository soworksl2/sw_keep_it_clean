from dataclasses import dataclass


@dataclass
class DirectoryInstructions:
    abs_path: str
    exclusion_items: list[str]
    life_time: int

    @staticmethod
    def from_json_dict(json_dict: dict) -> "DirectoryInstructions":
        abs_path = json_dict['abs_path']
        exclusion_items = json_dict.get('exclusion_items', [])

        if not isinstance(exclusion_items, list):
            raise Exception('the configuration file is bad formatted')

        life_time = json_dict.get('life_time', 30)

        if not isinstance(life_time, int):
            raise Exception('the configuration file is bad formatted')
        
        return DirectoryInstructions(abs_path, exclusion_items, life_time)
