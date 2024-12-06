import argparse
from time import time
from os.path import getsize

import server
import client
import archive
from misc import ran, format_size


parser = argparse.ArgumentParser()

parser.add_argument("--files", "-f", help="list of files and folders to be ziped and sent. To pass more than one file separate paths with a comma with no spaces", default = None)
parser.add_argument('-i', "--host-ip", help = "prints host's ip", required = False)
parser.add_argument("-u", '--unwrap-at', help = "choses folder to extract recieved file in", default = ".", required = False)
parser.add_argument("-w", "--wait", help = "waits for connection", action = "store_true", default = False, required = False)
parser.add_argument("-c", "--connect", help = "Connect to some waiting server and takes ipv4 address", type = str, default = None, required = False)

args = parser.parse_args()

if args.wait:
	sr = server.Server()
	print("waiting for incoming connection...")
	sr.accept(ran() + ".zip")

elif args.files and args.connect:
	items = args.files.split(",")
	archive_name = ran() + ".zip"

	archive.compress_some_shit(items, archive_name)

	cl = client.Client(args.connect)
	print(f"The size of files to be sent is {format_size(archive_name)}")
	print(f'sending {archive_name}...')

	cl.send_file(archive_name)

	print("file sent")

elif args.files is None and args.unwrap_at == '.':
	print(server.get_host_ip())