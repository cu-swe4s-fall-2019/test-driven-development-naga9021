import unittest
import math_lib
import statistics

class TestMathLib(unittest.TestCase):
    def test_list_mean_empty_list(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)
        
        
    def test_list_mean_empty_list(self):
        r = math_lin.list_mean([])
        self.assertEqual(r, None)
        
        
    def test_list_mean_constants(self):
        r = math_lib.list_mean([5, 5, 5, 5, 5, 5, 5, 5])
        self.assertEqual(r, 5)
        
        
    def test_list_mean_rand_ints(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(
                    random.randint(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertEqual(r, e)
        
        
    def test_list_mean_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(
                    random.uniform(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertTrue(math.isclose(r, e))
            
    
    def test_list_mean_non_int(self):
        L = []
        for i in range(10):
            L.append(random.randint(0, 100))
        L.append('Z')
        
        with self.assertRaises(ValueError) as ex:
            math_lib.list_mean(L)
            
        self.assertEqual(
            'Unsupported character within list.')
        
        
    def test_list_stdev_empty_list(self):
        r = math_lib.list_stdev(None)
        self.assertEqual(r, None)
        
        
    def test_list_stdev_empty_list(self):
        r = math_lin.list_stdev([])
        self.assertEqual(r, None)
        
        
    def test_list_stdev_constants(self):
        r = math_lib.list_stdev([5, 5, 5, 5, 5, 5, 5, 5])
        self.assertEqual(r, 0)   
        
        
    def test_list_stdev_rand_ints(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(
                    random.randint(0, 100))
            r = math_lib.list_stdev(L)
            e = statistics.stdev(L)
            self.assertEqual(r, e)
            
            
    def test_list_stdev_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(
                    random.uniform(0, 100))
            r = math_lib.list_stdev(L)
            e = statistics.stdev(L)
            self.assertTrue(math.isclose(r, e))
            
            
    def test_list_stdev_non_int(self):
        L = []
        for i in range(10):
            L.append(random.randint(0, 100))
        L.append('Z')
        
        with self.assertRaises(ValueError) as ex:
            math_lib.list_stdev(L)
            
        self.assertEqual(
            'Unsupported character within list.')
        
        
if __name__ == '__main__':
    unittest.main()
