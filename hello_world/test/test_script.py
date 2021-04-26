import unittest

class SimpleTest(unittest.TestCase):

	# Returns True or False.
	def test(self):
		self.assertTrue(True)

	def test_split(self):
        	s = 'hello world'
        	self.assertEqual(s.split(), ['hello', 'world'])
       		with self.assertRaises(TypeError):
            	s.split(2)

if __name__ == '__main__':
	unittest.main()
