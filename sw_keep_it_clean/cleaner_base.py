from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class CleanerBase(ABC):

    @abstractmethod
    def execute(self):
        pass
