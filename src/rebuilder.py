from ifaces import IRebuilder
from .workdir import WorkDir
from .termutils import under, info


class Rebuilder(IRebuilder):
    def __init__(self, workdir: WorkDir):
        self.__workdir = workdir

    def rebuild(self):
        info(f"rebuild package {under(self.__workdir.package_name)}")
