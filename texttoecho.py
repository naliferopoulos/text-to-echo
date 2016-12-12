#!/usr/bin/env python
#
# **************************************************************
#               Convert text to multiple echos
# **************************************************************
#
# Author: Nick Aliferopoulos
# aliferopoulos@icloud.com
#

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

class TextToEcho(object):
	def convert(self):
		print("Type away! :)")
		
		final = ""
		print "\t",
		text = raw_input()
	
		while(text != ""):
			final = final + "echo \"" + text + "\" \n"			
			print "\t",			
			text = raw_input()

		print("Done! Here are your echos!")
		print("")
		print(final)

def main():
    parser = ArgumentParser(description='Text to Echo', formatter_class = ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 1.0')
    args = parser.parse_args()

    tte = TextToEcho()
    tte.convert()

if __name__ == '__main__':
    main()
