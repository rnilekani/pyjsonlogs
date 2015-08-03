import sys
import os

import accesslog


def main():

	if len(sys.argv) < 3:
		print "Incorrect syntax. Usage: python main.py -f <filename>"
		sys.exit(2)

	elif sys.argv[1] != "-f":
		print "Invalid switch"
		sys.exit(2)
	elif os.path.isfile(sys.argv[2]) == False:
		print "File does not exist"
		sys.exit(2)

	accesslog.toJson(sys.argv[2])		


if __name__ == "__main__":
	main()
