import unittest # built in
import sample_function #imported file

class TestMain(unittest.TestCase): #class test - how its written

    def test_do_stuff(self): #making test functions
        test_param = 10
        result = sample_function.do_stuff(test_param)
        self.assertEqual(result, 50)

    def test_do_stuff2(self):
        test_param = 'abc'
        result = sample_function.do_stuff(test_param)
        self.assertIsInstance(result, ValueError) #asserting

    def test_do_stuff3(self):
        test_param = None
        result = sample_function.do_stuff(test_param)
        self.assertIsInstance(result, TypeError) #asserting
    
    def tearDown(self):
        print('cleaning up!')

if __name__ == '__main__':
    unittest.main()