#! /usr/bin/env/ python

def main():
	x = "hello world"
	wordlist = ["apple", "con", "concave", "jig", "jigsaw", "saw", "very", "zebra"]
	for word in wordlist:
		partA = word
		if partA in wordlist:
			
			print "true"
		else:
			print "false"

		print word

main()
