  1 import unittest
  2 import main
  3 
  4 class TestMain(unittest.TestCase):
  5     def test_do_stuff(self):
  6         test_param = 10
  7         result = main.do_stuff(test_param)
  8         self.assertEqual(result, 15)
  9 
 10     def test_do_stuff2(self):
 11         test_param = "abcdef"
 12         result = main.do_stuff(test_param)
 13         self.assertIsInstance(result, ValueError)
 14 
"test2.py" 32L, 859B