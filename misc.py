from crc import Calculator, Crc32
from os.path import getsize
from time import time

def ran() -> str:
	calc = Calculator(Crc32.CRC32)
	return hex(calc.checksum(str(int(time())).encode("latin-1"))).removeprefix("0x")

def format_size(filepath: str) -> str:
	size = getsize(filepath)
	suf = "b"

	if size >= 1024:
		size /= 1024
		suf="kb"

	if size >= 1024:
		size /= 1024
		suf="mb"

	if size >= 1024:
		size /= 1024
		suf="gb"

	if size >= 1024:
		size /= 1024
		suf="tb"
	
	return f"{size}{suf}"

def format_size_int(size: int) -> str:
	suf = "b"

	if size >= 1024:
		size /= 1024
		suf="kb"

	if size >= 1024:
		size /= 1024
		suf="mb"

	if size >= 1024:
		size /= 1024
		suf="gb"

	if size >= 1024:
		size /= 1024
		suf="tb"
	
	return f"{size}{suf}"