from abc import ABC, abstractmethod
from typing import List


class ISpecGen(ABC):
    @abstractmethod
    def generate(self) -> List[str]:
        pass
