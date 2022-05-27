from enum import Enum
import subprocess
import re

from .required import requiredpkgs


class RpmVersion(int, Enum):
    V3 = 3
    V4 = 4


class Rpm:
    def __init__(self):
        self.__version = self.__get_version()

    def __get_version(self) -> RpmVersion:
        version_regex = r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
        version = re.search(version_regex, self.__fetch_version())

        if version is None:
            raise RuntimeError("couldn't get RPM version")

        version = int(version["major"])
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
