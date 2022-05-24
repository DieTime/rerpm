import tempfile
import os
import atexit
import shutil

from .termutils import info, warn, under


class WorkDir:
    def __init__(self, package_path: str):
        self.__package_path = package_path
        self.__package_name = os.path.basename(package_path)

        self.__validate_package_file()
        self.__setup_directories()

    def __validate_package_file(self):
        if not os.path.isfile(self.package_path):
            raise RuntimeError(
                f"file doesn't exists: {under(self.package_name)}")

        if not self.package_path.endswith(".rpm"):
            raise RuntimeError(
                f"file is not rpm package: {under(self.package_name)}")

    def __setup_directories(self):
        tmpdir = tempfile.gettempdir()
        dir_name = self.package_name.replace(".rpm", "")

        path = os.path.join(tmpdir, "rerpm", dir_name)
        buildroot_path = os.path.join(path, "buildroot")

        if os.path.isdir(path):
            warn(f"cleanup previous working directory ...")
            shutil.rmtree(path)

        os.makedirs(buildroot_path)
        atexit.register(self.__cleanup)

        workdir_package_path = os.path.join(path, self.package_name)
        shutil.copy2(self.__package_path, path)

        self.__path = path
        self.__buildroot_path = buildroot_path
        self.__package_path = workdir_package_path

    def __cleanup(self):
        if os.path.isdir(self.__path):
            info("cleanup working directory ...")
            shutil.rmtree(self.__path)

    @property
    def path(self) -> str:
        return self.__path

    @property
    def buildroot_path(self) -> str:
        return self.__buildroot_path

    @property
    def package_path(self) -> str:
        return self.__package_path

    @property
    def package_name(self) -> str:
        return self.__package_name

    @property
    def cpio_path(self) -> str:
        return os.path.join(self.__path, self.cpio_name)

    @property
    def cpio_name(self) -> str:
        return self.__package_name.replace(".rpm", ".cpio")
