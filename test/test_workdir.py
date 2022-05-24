import atexit
import unittest
import tempfile
import os

from src import WorkDir


class TestWorkDir(unittest.TestCase):
    def test_positive(self):
        package_name = "rpm-4.18.0-0.alpha2.2.mga9.x86_64.rpm"
        package_path = f"test/assets/{package_name}"
        workdir = WorkDir(package_path)

        tmp_dir = tempfile.gettempdir()
        package_dir = package_name.replace(".rpm", "")

        work_dir_path = os.path.join(tmp_dir, "rerpm", package_dir)
        work_dir_package_path = os.path.join(work_dir_path, package_name)
        buildroot_path = os.path.join(
            tmp_dir, "rerpm", package_dir, "buildroot")

        self.assertEqual(work_dir_path, workdir.path)
        self.assertEqual(buildroot_path, workdir.buildroot_path)
        self.assertEqual(package_name, workdir.package_name)
        self.assertEqual(work_dir_package_path, workdir.package_path)

        self.assertTrue(os.path.isdir(workdir.path))
        self.assertTrue(os.path.isdir(workdir.buildroot_path))
        self.assertTrue(os.path.isfile(workdir.package_path))

    def test_file_not_exist(self):
        self.assertRaises(RuntimeError, WorkDir, "not_exist.rpm")

    def test_file_not_rpm(self):
        broken_ext_file = "rpm-4.18.0-0.alpha2.2.mga9.x86_64.not_rpm"
        self.assertRaises(RuntimeError, WorkDir,
                          f"test/assets/{broken_ext_file}")

    def test_remove_workdir(self):
        package_name = "rpm-4.18.0-0.alpha2.2.mga9.x86_64.rpm"
        package_path = f"test/assets/{package_name}"

        workdir = WorkDir(package_path)
        workdir_path = workdir.path

        self.assertTrue(os.path.isdir(workdir_path))
        atexit._run_exitfuncs()
        self.assertFalse(os.path.isdir(workdir_path))


if __name__ == "__main__":
    unittest.main()
