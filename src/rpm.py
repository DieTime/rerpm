from enum import Enum
import subprocess

from .required import requiredpkgs


class RpmVersion(int, Enum):
    V3 = 3
    V4 = 4


class Rpm:
    def __init__(self):
        self.__version = self.__get_version()

    def __get_version(self) -> RpmVersion:
        version_tokens = self.__fetch_version().split()
        if len(version_tokens) < 3:
            raise RuntimeError("couldn't get RPM version")

        version = int(version_tokens[2].split('.')[0])
        if version not in [RpmVersion.V3, RpmVersion.V4]:
            raise RuntimeError(f"unsupported RPM version: v{version}")

        return RpmVersion(version)

    @requiredpkgs(["rpm"])
    def __fetch_version(self) -> str:
        command = subprocess.run(["rpm", "--version"],
                                 capture_output=True, check=True)
        return command.stdout.decode("utf-8")

    @property
    def version(self) -> RpmVersion:
        return self.__version
