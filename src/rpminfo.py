from enum import Enum
import subprocess

from .required import requiredpkgs


class RPMVersion(int, Enum):
    V3 = 3
    V4 = 4


class RPMInfo:
    def __init__(self):
        self.__version = self.__get_version()

    @requiredpkgs(["rpm"])
    def __get_version(self) -> RPMVersion:
        command = subprocess.run(["rpm", "--version"],
                                 capture_output=True, check=True)

        output_list = command.stdout.decode("utf-8").split()
        if len(output_list) < 3:
            raise RuntimeError("couldn't get RPM version")

        version = int(output_list[2].split('.')[0])
        if version not in [RPMVersion.V3, RPMVersion.V4]:
            raise RuntimeError(f"unsupported RPM version: v{version}")

        return RPMVersion(version)

    @property
    def version(self) -> RPMVersion:
        return self.__version
