import unittest
from hello_world.app import lambda_handler

class SimpleTest(unittest.TestCase):
			
	def test_message(self):
		result=lambda_handler()
		self.assertEqual(result, "hellow world")

if __name__ == '__main__':
	unittest.main()
