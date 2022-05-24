from abc import ABC, abstractmethod


class IRebuilder(ABC):
    @abstractmethod
    def rebuild(self):
        pass
