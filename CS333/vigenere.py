
from string import ascii_uppercase, ascii_letters


MessageSymbols = ascii_uppercase
KeySymbols = ascii_uppercase


class VigenereCipher:

	# ////////////////////////
	# PUBLIC
	# ////////////////////////

	def encrypt(self, message, key):
		self.message = message
		self.key = key.upper()
		self.mode = 'encrypt'
		return ''.join(self.translate()) 

	def decrypt(self, message, key):
		self.message = message
		self.key = key.upper()
		self.mode = 'decrypt'
		return ''.join(self.translate())

	# ////////////////////////
	# INHERITED
	# ////////////////////////

	def translate(self):
		translated = []
		self.key_index = 0

		for symbol in self.message:
			
			translated.append(self.getTranslatedSymbol(symbol))

			self.updateKeyIndex()

		return translated

	def updateKeyIndex(self):
		self.key_index += 1 
		if self.key_index == len(self.key):
			self.key_index = 0

	# ////////////////////////
	# VIRTUAL
	# ////////////////////////

	def getTranslatedSymbol(self, symbol):
		if type(symbol) != str:
			symbol = chr(symbol)

		if not self.isValid(symbol):
			return symbol

		index = self.getIndex(symbol)
		return MessageSymbols[index] if symbol.isupper() else MessageSymbols[index].lower()

	# ////////////////////////
	# HELPERS
	# ////////////////////////

	def isValid(self, symbol):
		return symbol.upper() in MessageSymbols

	def getIndex(self, symbol):
		return (MessageSymbols.index(symbol.upper())
			+ self.indexChange()) % len(MessageSymbols) # handles wrap-arounds 

	def indexChange(self):
		sign = 1 if self.mode == 'encrypt' else -1
		return KeySymbols.index(self.key[self.key_index]) * sign
