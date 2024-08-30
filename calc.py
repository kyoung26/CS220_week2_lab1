
class add:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def math(self):
        return self.x + self.y
    
        
class multiply(add):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def math(self):
        return self.x * self.y
            
import unittest


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        addition = add(3,3)
        self.assertEqual(addition.math(), 6)
        
    def test_multiply(self):
        multiplication = multiply(3,3)
        self.assertEqual(multiplication.math(), 9)
        
if __name__ == "__main__":
    unittest.main()


            
