import os
import subprocess

from .workdir import WorkDir
from .termutils import under, info
from .required import requiredpkgs

class Unpacker:
    def __init__(self, workdir: WorkDir):
        self.__workdir = workdir

    def unpack(self):
        self.__rpm_to_cpio()
        self.__cpio_to_data()
        info(f"package unpacked to {under(self.__workdir.buildroot_path)} directory")

    @requiredpkgs(["rpm2cpio"])
    def __rpm_to_cpio(self):
        with open(self.__workdir.cpio_path, mode='w+') as cpio:
            subprocess.run(["rpm2cpio", self.__workdir.package_path],
                           stdout=cpio, check=True)

    @requiredpkgs(["cpio"])
    def __cpio_to_data(self):
        current_dir = os.getcwd()
        os.chdir(self.__workdir.buildroot_path)

        with open(self.__workdir.cpio_path) as cpio:
            with open(os.devnull) as devnull:
                subprocess.run(["cpio", "-idmu", "--no-absolute-filenames"], stdin=cpio,
                               stdout=devnull, stderr=devnull, check=True)

        os.chdir(current_dir)
