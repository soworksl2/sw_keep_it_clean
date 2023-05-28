import os
import shutil
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

from cleaner_base import CleanerBase
from clean_instructions import CleanInstruction
from directory_instructions import DirectoryInstructions
import sw_log


class ItemCleanState(Enum):
    NO_TO_CLEAN = 0
    ALMOST_TO_CLEAN = 1
    HAVE_TO_CLEAN = 2

@dataclass
class NormalCleaner(CleanerBase):
    clean_instrutions: CleanInstruction
    
    def execute(self):
        self._clean_directories()

    def _clean_directories(self):
        for directory_instructions in self.clean_instrutions.directories_instrucions:
            self._clean_directory(directory_instructions)

    def _clean_directory(self, directory_instructions: DirectoryInstructions):
        directory_path = directory_instructions.abs_path

        if not os.path.isdir(directory_path):
            sw_log.log(f'the specified directory "{directory_instructions.abs_path}" does not exists.')
            return

        all_items_in_dir = os.listdir(directory_path)
        abs_path_items_in_dir = [os.path.join(directory_path, item) for item in all_items_in_dir]

        for abs_item_path in abs_path_items_in_dir:
            item_state = self._analize_item_state(abs_item_path, directory_instructions)

            if item_state == ItemCleanState.NO_TO_CLEAN:
                continue
            elif item_state == ItemCleanState.ALMOST_TO_CLEAN:
                sw_log.log(f'the item "{abs_item_path}" will be deleted soon')
                continue
            else:
                sw_log.log(f'the item "{abs_item_path}" has been deleted')
                self._clean_item(abs_item_path)

    def _analize_item_state(self, abs_item_path: str, directory_instructions: DirectoryInstructions) -> ItemCleanState:
        if os.path.basename(abs_item_path) in directory_instructions.exclusion_items:
            return ItemCleanState.NO_TO_CLEAN

        creation_date = os.path.getctime(abs_item_path)
        creation_date = datetime.fromtimestamp(creation_date)

        today = datetime.now()

        lived_time = (today - creation_date).days
        life_time_completion = lived_time/directory_instructions.life_time

        if life_time_completion >= 1:
            return ItemCleanState.HAVE_TO_CLEAN
        elif life_time_completion >= 0.80:
            return ItemCleanState.ALMOST_TO_CLEAN
        else:
            return ItemCleanState.NO_TO_CLEAN

    def _clean_item(self, abs_item_path: str):
        if os.path.isdir(abs_item_path):
            shutil.rmtree(abs_item_path, True)
        else:
            os.remove(abs_item_path)
