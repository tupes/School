
from unittest import TestCase, main
from string import ascii_uppercase, ascii_letters

from frequency_analysis import FrequencyAnalyzer, englishFreqMatchScore
from vigenere import VigenereCipher
from detect_english import getEnglishCount
from utilities import removeTextNonLetters


class TestFrequencyAnalysis(TestCase):

	def setUp(self):
		self.analyzer = FrequencyAnalyzer(VigenereCipher(), ascii_uppercase)
		self.analyzer.message = removeTextNonLetters("Ppqca xqvekg ybnkmazu ybngbal jon i tszm jyim. Vrag voht vrau c tksg. Ddwuo xitlazu vavv raz c vkb qp iwpou.")
		self.analyzer.key_length = 4
		
		self.subkey_messages = ['PAEBABANZIAHAKDXAAAKIU', 'PXKNZNLIMMGTUSWIZVZBW', 'QQGKUGJTJVVVCGUTUVCQP', 'CVYMYBOSYRORTDOLVRVPO']
		self.subkey_score = [('A', 2), ('I', 2), ('N', 2), ('W', 2), ('X', 2), ('B', 1), ('C', 1), ('E', 1), ('G', 1), ('H', 1), ('K', 1), ('M', 1), ('O', 1), ('P', 1), ('R', 1), ('S', 1), ('T', 1), ('U', 1), ('V', 1), ('D', 0), ('F', 0), ('J', 0), ('L', 0), ('Q', 0), ('Y', 0), ('Z', 0)]

	def test_getNthSubkeyMessage(self):
		subkey_messages = [''.join(self.analyzer.getNthSubkeyMessage(n))
			for n in range(1, self.analyzer.key_length + 1)]
		self.assertEqual(subkey_messages, self.subkey_messages)

	def test_getSubkeyFreqScores(self):
		message = self.subkey_messages[0]
		self.assertEqual(self.analyzer.getSubkeyFreqScores(message), self.subkey_score)

	def test_englishFreqMatchScore(self):
		message = "Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm"
		self.assertEqual(englishFreqMatchScore(message), 5)
		message = "I rc ascwuiluhnviwuetnh,osgaa ice tipeeeee slnatsfietgi tittynecenisl. e fo f fnc isltn sn o a yrs sd onisli ,l erglei trhfmwfrogotn,l stcofiit.aea wesn,lnc ee w,l eIh eeehoer ros iol er snh nl oahsts ilasvih tvfeh rtira id thatnie.im ei-dlmf i thszonsisehroe, aiehcdsanahiec gv gyedsB affcahiecesd d lee onsdihsoc nin cethiTitx eRneahgin r e teom fbiotd n ntacscwevhtdhnhpiwru"
		self.assertEqual(englishFreqMatchScore(message), 9)


class TestDetectEnglish(TestCase):

	def test_is_english(self):	
		with open('data/book_plaintext.txt') as f:
			message = f.read()
		self.assertTrue(getEnglishCount(message))


if __name__ == '__main__':
	main()