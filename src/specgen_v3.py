import subprocess
from typing import List
from ifaces import ISpecGen

from .termutils import under, info
from .workdir import WorkDir


class SpecGenV3(ISpecGen):
    def __init__(self, workdir: WorkDir):
        self.__workdir = workdir

    def generate(self):
        info(f"generate spec file for {under(self.__workdir.package_name)} unsing rpm v3")
        return []

