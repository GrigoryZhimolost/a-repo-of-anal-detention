from os.path import isfile, isdir, join, basename
from os import remove, listdir, mkdir
from shutil import make_archive
from zipfile import ZipFile, ZIP_BZIP2

def compress_some_shit(items: list[str], arcname: str, mark_folders: bool = True): #arcname should be with extension
	with ZipFile(arcname, "w", ZIP_BZIP2) as arc:
		for i in items:
			if isfile(i):
				arc.write(i)
			else:
				if mark_folders:
					make_archive(f"anal-folder228{i}", "zip", i)
					arc.write(f'./anal-folder228{basename(i)}.zip')
					remove(f"./anal-folder228{basename(i)}.zip")
				else:
					make_archive(i, "zip", i)
					arc.write(f'{basename(i)}.zip')
					remove(f"./{basename(i)}.zip")


def decompress_some_shit(arcpath: str, destination: str, unroll_marked_folders: bool = True):
	with ZipFile(arcpath, "r", ZIP_BZIP2) as arc:
		arc.extractall(destination)
	
	if unroll_marked_folders:
		for i in listdir(destination):
			des = join(destination, i)
			if isfile(des) and i.endswith(".zip"):
				if i.startswith("anal-folder228"):

					j = join(destination, i.removeprefix("anal-folder228").removesuffix(".zip"))
					mkdir(j)
					with ZipFile(des, 'r', ZIP_BZIP2) as arc:
						arc.extractall(j)

					remove(join(destination, i))