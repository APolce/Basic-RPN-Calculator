import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)

	def test_sub(self):
		result = rpn.calculate("4 3 -")
		self.assertEqual(1, result)

	def test_mul(self):
		result = rpn.calculate("4 3 *")
		self.assertEqual(12, result)

	def test_div(self):
		result = rpn.calculate("4 2 /")
		self.assertEqual(2, result)

	def test_chain(self):
		result = rpn.calculate("1 1 + 2 *")
		self.assertEqual(4, result)

	def test_exp(self):
		result = rpn.calculate("2 3 ^")
		self.assertEqual(8, result)

	def test_percent(self):
		result = rpn.calculate("3 5 %")
		self.assertEqual(60, result)

	def test_int_division(self):
		result = rpn.calculate("5 2 //")
		self.assertEqual(2, result)

	def test_bitwise_and(self):
		result = rpn.calculate("22 12 &")
		self.assertEqual(4, result)
		result = rpn.calculate("14 12 &")
		self.assertEqual(12, result)

	def test_bitwise_or(self):
		result = rpn.calculate("22 12 |")
		self.assertEqual(30, result)
		result = rpn.calculate("14 12 |")
		self.assertEqual(14, result)

	def test_bitwise_not(self):
		result = rpn.calculate("22 ~")
		self.assertEqual(-23, result)
		result = rpn.calculate("14 ~")
		self.assertEqual(-15, result)