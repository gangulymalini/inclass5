import unittest
import test


class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(test.leapyeartest(123), False)
    def test_2(self):
        self.assertEqual(test.leapyeartest(4), False)
    def test_3(self):
        self.assertEqual(test.leapyeartest(100), False)
    def test_4(self):
        self.assertEqual(test.leapyeartest(1200), True)
    def test_5(self):
        self.assertEqual(test.leapyeartest(20), True)

if __name__ == "__main__":
    unittest.main()


def test_1():
    assert(not test.leapyeartest(123))
def test_2(self):
    assert(not test.leapyeartest(4))
def test_3(self):
    assert(not test.leapyeartest(100))
def test_4(self):
    assert(test.leapyeartest(1200))
def test_5(self):
    assert(test.leapyeartest(20))