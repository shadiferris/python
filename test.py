import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to run a function')
    def test_do_stuff(self):
        '''This is the first test'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        '''adding a comment to show more information about the test'''
        test_param = "abcdef"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter number!!")
        

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter number!!")

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('clearing up')

if __name__ == '__main__':
    unittest.main()
