import unittest
import os

from src import WorkDir, Unpacker


class TestUnpacker(unittest.TestCase):
    def test_positive(self):
        package_path = "test/assets/rpm-4.18.0-0.alpha2.2.mga9.x86_64.rpm"
        workdir = WorkDir(package_path)

        unpacker = Unpacker(workdir)
        unpacker.unpack()

        self.assertTrue(len(os.listdir(workdir.buildroot_path)) != 0)


if __name__ == "__main__":
    unittest.main()
