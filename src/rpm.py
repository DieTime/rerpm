from enum import Enum
import subprocess

from .required import requiredpkgs


class RpmVersion(int, Enum):
    V3 = 3
    V4 = 4


class Rpm:
    def __init__(self):
        self.__version = self.__get_version()

    @requiredpkgs(["rpm"])
    def __get_version(self) -> RpmVersion:
        command = subprocess.run(["rpm", "--version"],
                                 capture_output=True, check=True)

        output_list = command.stdout.decode("utf-8").split()
        if len(output_list) < 3:
            raise RuntimeError("couldn't get RPM version")

        version = int(output_list[2].split('.')[0])
        if version not in [RpmVersion.V3, RpmVersion.V4]:
            raise RuntimeError(f"unsupported RPM version: v{version}")

        return RpmVersion(version)

    @property
    def version(self) -> RpmVersion:
        return self.__version
