import base64
import sys


def write_file(data, file_path):
	""" Helper function to store data in a file """
	try:
		with open(file_path, "w") as f:
			f.write(data)
	except Exception as err:
		print(f"error writing data to local file at {file_path}: {err}")
		sys.exit()

	return data


def read_file(file_path):
	""" Helper function to load data from a file """
	data = b''
	try:
		with open(file_path) as f:
			data = f.read()
	except Exception as err:
		print(f"error reading data from local file at {file_path}: {err}")
		sys.exit()

	return data


def validate(args):
	for k, v in args.items():
		if len(v) > 0:
			continue

		print(f"{k} cannot be empty")
		sys.exit()


def encode(x):
	return base64.b64encode(s.encode()).decode()


def decode(x):
	return base64.b64decode(x.encode()).decode()
