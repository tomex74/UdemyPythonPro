import unittest

import vector

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.v1 = vector.Vector(0, 0)
        self.v2 = vector.Vector(-1, 1)
        self.v3 = vector.Vector(2.5, -2.5)

    def test_equality(self):
        self.assertNotEqual(self.v1, self.v2)
        expected_result = vector.Vector(-1, 1)
        self.assertEqual(self.v2, expected_result)

    def test_add(self):
        result = self.v1 + self.v2
        expected_result = vector.Vector(-1, 1)
        self.assertEqual(result, expected_result)

    def test_sub(self):
        result = self.v2 - self.v3
        expected_result = vector.Vector(-3.5, 3.5)
        self.assertEqual(result, expected_result)

    def test_mul(self):
        result = self.v1 * 5
        expected_result = vector.Vector(0.0, 0.0)
        self.assertEqual(result, expected_result)
        result = self.v1 * self.v2
        expected_result = 0.0
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()
