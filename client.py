import socket
from crpt import Cipher
from math import ceil
from os.path import getsize
from config import PORT

class Client:
	def __init__(self, ip):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((ip, PORT))
		self.ch = Cipher()
	
	def send_file(self, path: str):
		file_size = ceil(getsize(path) / 2048)
		size, nonce = self.ch.encrypt(file_size.to_bytes())
		self.sock.send(size + nonce)

		with open(path, "rb") as file:
			while True:
				chunck = file.read(2048)

				if not chunck:
					break

				chunck, nonce = self.ch.encrypt(chunck)

				self.sock.send(chunck + nonce)

	def __del__(self):
		self.sock.close()
