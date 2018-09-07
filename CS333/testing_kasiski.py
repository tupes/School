
from unittest import TestCase, main
from collections import Counter

from kasiski_examination import *
from utilities import removeTextNonLetters, removeBinaryNonLetters


class TestKasiskiFactors(TestCase):

	def setUp(self):
		self.message = removeTextNonLetters("Ppqca xqvekg ybnkmazu ybngbal jon i tszm jyim. Vrag voht vrau c tksg. Ddwuo xitlazu vavv raz c vkb qp iwpou.")
		self.seq_spacings = {'AZU': [48], 'VRA': [8, 32, 24], 'YBN': [8]}
		self.seq_factors = {
			'AZU': [2, 3, 4, 6, 8, 12, 16],
 			'VRA': [8, 2, 4, 8, 16, 2, 4, 2, 3, 4, 6, 8, 12],
 			'YBN': [8, 2, 4]}
		self.factor_counts = Counter({2: 5, 4: 5, 8: 5, 16: 2, 3: 2, 6: 2, 12: 2})

	def test_getRepeatedSeqSpacings(self):
		self.assertEqual(getRepeatedSeqSpacings(self.message), self.seq_spacings)

	def test_getSeqFactors(self):
		self.assertEqual(getSeqFactors(self.seq_spacings), self.seq_factors)

	def test_getFactorCounts(self):
		self.assertEqual(getFactorCounts(self.seq_factors), self.factor_counts)


class TestKasiskiExamination(TestCase):

	def setUp(self):
		self.likely_key_lengths = [3, 2, 6, 4, 12, 8, 9, 16, 5, 11, 10, 15, 7, 14, 13]

	def test_kasiskiExamination_text(self):
		with open('data/book_ciphertext.txt') as f:
			ciphertext = removeTextNonLetters(f.read())
		self.assertEqual(kasiskiExamination(ciphertext), self.likely_key_lengths)

	def test_kasiskiExamination_binary(self):
		with open('data/book_cipherbytes', 'rb') as f:
			cipherbytes = removeBinaryNonLetters(f.read())
		self.assertEqual(kasiskiExamination(cipherbytes), self.likely_key_lengths)


if __name__ == '__main__':
	main()