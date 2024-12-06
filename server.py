import socket

from crpt import Cipher
from config import PORT
from misc import format_size_int

def get_host_ip() -> str:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]

class ConnectionAbortedFileNotSentError(Exception):
	pass

class Server:
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((get_host_ip(), PORT))
		self.ch = Cipher()
	
	def accept(self, file_path: str):
		self.sock.listen(1)
		conn, addr = self.sock.accept()
		print(f'{addr} connected')
		'''pa = self.ch.decrypt(conn.recv(16))
		pa = int.from_bytes(self.ch.decrypt(pa[:8], pa[8:]))'''

		#print(f'File size to be received: {format_size_int(pa)}')
		print(f"A file will be received({file_path})")

		with open(file_path, "wb") as file:
			while True:
				data = conn.recv(2056)
				if not data:
					break
				if len(data) == 2056:
					nonce = data[2048:]
					file.write(self.ch.decrypt(data[:2048], nonce))
				else:
					print(len(data), len(data[:len(data)-8]))
					nonce = data[len(data) - 8:]
					file.write(self.ch.decrypt(data[:len(data)-8], nonce))
		try:
			conn.send("228".encode("utf8"))
		except:
			pass

		conn.close()

	def __del__(self):
		self.sock.close()