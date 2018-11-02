import unittest

from mymatrix import MyMatrix

class TestMyMatrix(unittest.TestCase):
    def test_get(self):
        m = MyMatrix(3, 5)
        self.assertEqual(m.get(1, 1), 6)
