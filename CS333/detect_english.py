
from string import ascii_letters

SYMBOLS = ascii_letters + ' \t\n'

ENGLISH_WORDS = {word.strip() for word in open('data/dictionary.txt')}


def isEnglish(message, word_percentage=20, letter_percentage=85):
	if getEnglishCount(message) * 100 < word_percentage:
		return False

	return len([x for x in message if x in SYMBOLS]) / len(message) * 100 >= letter_percentage

def getEnglishCount(message):
	message = message.upper()
	possible_words = message.split()
	message = ''.join([x for x in message if x in SYMBOLS])
	english_count = len([1 for word in possible_words if word in ENGLISH_WORDS])
	return english_count / len(possible_words)
