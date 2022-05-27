import argparse

from src import *
from ifaces import *


def process(args: argparse.Namespace):
    workdir = WorkDir(args.rpmfile)
    info(f"start rebuilding {under(workdir.package_name)}")

    rpm = Rpm()

    unpacker = Unpacker(workdir)
    rebuilder = Rebuilder(workdir)
    specgen = {
        RpmVersion.V3: SpecGenV3,
        RpmVersion.V4: SpecGenV4
    }[rpm.version](workdir)

    rerpm = Rerpm(unpacker, specgen, rebuilder)
    rerpm.process()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PRM packages rebuilder')
    parser.add_argument('rpmfile', metavar='RPM', type=str,
                        help='RPM package file path')
    args = parser.parse_args()

    try:
        process(args)
    except Exception as message:
        error(str(message))
