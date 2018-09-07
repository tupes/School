
from string import ascii_letters
import re

NONLETTERS_PATTERN = re.compile('[^A-Z]')


def removeTextNonLetters(message):
	return NONLETTERS_PATTERN.sub('', message.upper())

def removeBinaryNonLetters(message):
	return ''.join([chr(b).upper() for b in message if chr(b) in ascii_letters])

def getInBothCount(s1, s2):
	return len({x for x in s1} & {y for y in s2})

# ############################
# UTILITY CONVERSION FUNCTIONS
# ############################

hexDigits = "0123456789ABCDEF"

def getHexString(_string):
    return hex(ord(_string))

def getPaddedHexString(_int):
	h = hex(_int)
	return h if len(h) > 3 else '0x0' + h[-1]

def getChar(_hex):
    return chr(int(_hex, 16))

def getHigherHex(string):
    return getHex(string[2])

def getLowerHex(string):
    return getHex(string[3])

def getHex(char):
    return int("0x0" + char, 16)

def convertToHex(ch, cl):
    return "0x"+ hexDigits[ch] + hexDigits[cl]

def getBinary(char):
    return bytes.fromhex(hex(ord(char))[2:])

def getBinary(char):
    return bytes.fromhex(char[2:])

def getSymbol(symbol):
	return symbol if type(symbol) == str else chr(symbol)
