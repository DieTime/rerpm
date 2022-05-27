import unittest

from src import Rpm, RpmVersion


def mock_fetch_version_v3() -> str:
    return "RPM version 3.14.2"


def mock_fetch_version_v4() -> str:
    return "RPM version 4.14.2"


def mock_fetch_version_v5() -> str:
    return "RPM version 5.14.2"


def mock_fetch_version_short_v3() -> str:
    return "3.2.1"


def mock_fetch_version_any_v4() -> str:
    return "v4.2.1 RPM"


def mock_fetch_version_incorrect() -> str:
    return "RPM version 4.2"


class TestRpm(unittest.TestCase):
    def test_v3(self):
        rpm = Rpm()
        rpm._Rpm__fetch_version = mock_fetch_version_v3
        self.assertEqual(rpm._Rpm__get_version(), RpmVersion.V3)

    def test_v4(self):
        rpm = Rpm()
        rpm._Rpm__fetch_version = mock_fetch_version_v4
        self.assertEqual(rpm._Rpm__get_version(), RpmVersion.V4)

    def test_v5(self):
        rpm = Rpm()
        rpm._Rpm__fetch_version = mock_fetch_version_v5
        self.assertRaises(RuntimeError, rpm._Rpm__get_version)

    def test_short_v3(self):
        rpm = Rpm()
        rpm._Rpm__fetch_version = mock_fetch_version_short_v3
        self.assertEqual(rpm._Rpm__get_version(), RpmVersion.V3)

    def test_any_v4(self):
        rpm = Rpm()
        rpm._Rpm__fetch_version = mock_fetch_version_any_v4
        self.assertEqual(rpm._Rpm__get_version(), RpmVersion.V4)

    def test_incorrect(self):
        rpm = Rpm()
        rpm._Rpm__fetch_version = mock_fetch_version_incorrect
        self.assertRaises(RuntimeError, rpm._Rpm__get_version)


if __name__ == "__main__":
    unittest.main()
