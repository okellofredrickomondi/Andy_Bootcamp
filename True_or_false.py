import unittest

class SimplisticTest(unittest.TestCase):
	def truest(self):
		self.assertTrue(True)

	def not_true(self):
		self.assertFalse(False)

	if __name__ == '__main__':
		unittest.main()
"""
true or false
"""