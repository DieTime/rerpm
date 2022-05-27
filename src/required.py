import functools
import subprocess
from typing import List

from .termutils import under


def requiredpkgs(packages: List[str]):
    assert(len(packages) > 0)

    def check_package(package: str):
        check = subprocess.run(["which", package], capture_output=True)
        if check.returncode != 0:
            raise RuntimeError(f"please install {under(package)} package")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for package in packages:
                check_package(package)

            return func(*args, **kwargs)
        return wrapper
    return decorator
