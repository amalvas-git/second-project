import unittest
import hello_world.app

class SimpleTest(unittest.TestCase):
			
	def test_message(self):
		result=app.lambda_handler()
		self.assertEqual(result, "hellow world")

if __name__ == '__main__':
	unittest.main()
