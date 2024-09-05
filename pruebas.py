import unittest

class Test_examples(unittest.TestCase):

    def test_equals(self):
        a = 1
        b = True
        self.assertEqual(a,b)
    
    def test_bool_equal(self):
        self.assertEqual(True, not False)

    def test_not_equals(self):
        a=1
        b=2
        self.assertNotEqual(a,b)

    def test_is_true(self):
        a = True
        b = not False  
        self.assertTrue(a == b)
    
    def test_is_false(self):
        a = True
        b = False
        self.assertFalse(a == b)

    def test_is_none(self):
        a = None
        self.assertIsNone(a)

    def test_is_more(self):
        a = 'a'
        b = 'bb'
        self.assertGreater(b,a)
    
    def test_is_less(self):
        a = 1
        b = 2
        self.assertLess(a,b)

    def test_is_more_equal(self):
        a = 2
        b = 1
        self.assertGreaterEqual(a,b)

    def test_is_less_equal(self):
        a = 1
        b = 2
        self.assertLessEqual(a,b)

    def test_list_is_equal(self):
        a = [1,1,1,1,1,1,1]
        for i in range(1,len(a)):
            self.assertEqual(a[i-1],a[i])

if __name__ == '__main__':
    unittest.main()
    #ok