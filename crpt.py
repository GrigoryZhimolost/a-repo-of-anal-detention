from Crypto.Cipher import ChaCha20

from config import KEY


class Cipher:
	def __init__(self):
		self.ch = ChaCha20.new(key=KEY)
	
	def encrypt(self, data: bytes):
		return self.ch.encrypt(data), self.ch.nonce
	
	def decrypt(self, data: bytes, nonce) -> bytes:
		self.ch = ChaCha20.new(key=KEY, nonce=nonce)
		return self.ch.decrypt(data)