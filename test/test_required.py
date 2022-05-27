import unittest

from src import requiredpkgs


class TestRequired(unittest.TestCase):
    def test_positive(self):
        try:
            self.__postitive()
        except Exception:
            self.fail()

    def test_negative(self):
        self.assertRaises(RuntimeError, self.__negative)

    def test_multiple_positive(self):
        try:
            self.__multiple_postitive()
        except Exception:
            self.fail()

    def test_multiple_negative(self):
        self.assertRaises(RuntimeError, self.__multiple_negative)

    @requiredpkgs(["which"])
    def __postitive(self):
        pass

    @requiredpkgs(["unknown!!!"])
    def __negative(self):
        pass

    @requiredpkgs(["which", "cat", "ls"])
    def __multiple_postitive(self):
        pass

    @requiredpkgs(["which", "cat", "ls", "unknown!!!"])
    def __multiple_negative(self):
        pass


if __name__ == "__main__":
    unittest.main()
