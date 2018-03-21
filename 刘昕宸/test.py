from hello import *
import unittest

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2, add(1,2))
        self.assertNotEqual(2, add(3,4))

if __name__ == '__main__':
    unittest.main()
        
        

    