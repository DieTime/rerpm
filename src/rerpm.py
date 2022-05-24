from ifaces import ISpecGen, IRebuilder
from .unpacker import Unpacker


class Rerpm:
    def __init__(self, unpacker: Unpacker, specgen: ISpecGen, rebuilder: IRebuilder):
        self.__unpacker = unpacker
        self.__specgen = specgen
        self.__rebuilder = rebuilder

    def process(self):
        self.__unpacker.unpack()
        self.__specgen.generate()
        self.__rebuilder.rebuild()
