#!/usr/bin/python3.6

from optparse import OptionParser
from optioncomplete import autocomplete
import subprocess,sys
from subprocess import PIPE, Popen
from time import sleep
import argcomplete

ncolr = '\x1b[0m'
colr = '\x1b[33;92m'

def steghideuse(filepath, image):
	print ("*****************************************************************************")
	print ("** Wordlist	: %s " % filepath)
	print ("** Author	: ChathuraDR ")
	print ("*****************************************************************************")

	print ("[*] Reading the wordlist...")
	try:
		with open(filepath) as fp:
			line = fp.readline()
			print("[*] Start attacking....")
			while line:
				pwd = line.strip()
				print("\r[*] Checking : %s                            " % pwd, end="")
				sys.stdout.flush()
				sleep(0.1)
				p = subprocess.Popen(["steghide", "extract", "-sf", image, "-p", pwd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				stdout_value = p.communicate()[0].decode('ascii')
				if not stdout_value == "steghide: could not extract any data with that passphrase!\n":
					sleep(0.1)
					sys.stdout.write(ncolr+ "\n[*] Password is : " + colr + pwd + ncolr)
					print("\n[*] Image is successfully extracted!")
					quit()
				line = fp.readline()
	except Exception as e:
		print("[*] File not found!")

usage="Usage: steghidebruteforce -w... [WORDLIST]... -i.... [IMAGE] \nDictionary attack on a image using steghide."
parser=OptionParser(usage=usage)
parser.add_option("-w", "--wordlist", dest="wordlist", action="store_true", default=False, help="Select your wordlist")
parser.add_option("-i", "--image", dest="image", action="store_true", default=False, help="Select the Image")
argcomplete.autocomplete(parser,sys.argv[0])
(opts,args) = parser.parse_args()

if opts.wordlist and opts.image:
	steghideuse(args[0],args[1])
elif not opts.wordlist and opts.image:
	print("[*] Wordlist is not given")
elif opts.wordlist and not opts.image:
        print("[*] Image is not given")
else:
	print("[*] Wordlist or Image not given")

