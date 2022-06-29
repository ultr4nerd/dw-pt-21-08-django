"""Class of testing"""

import unittest


def suma(num_1: int, num_2: int) -> int:
    """Add two numbers"""
    return num_1 + num_2


class TestAritmetica(unittest.TestCase):
    """Test arithmetic operations"""

    def test_suma(self):
        """Test suma"""
        resultado = suma(5, 5)
        self.assertEqual(resultado, 10)


if __name__ == "__main__":
    unittest.main()
