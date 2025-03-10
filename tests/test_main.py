import unittest
from app.main import soma, multiplica

class TestFuncoes(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        
    def test_multiplica(self):
        self.assertEqual(multiplica(2, 3), 6)
        self.assertEqual(multiplica(-1, 5), -5)

if __name__ == "__main__":
    unittest.main()
