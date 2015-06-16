#! /usr/bin/env/ python
#M. Sivananthan

import string

def main():
	wordlist = ["apple", "con", "cave", "concave", "jig", "jigsaw", "saw", "very", "zebra"]
	specialList = []

	for substringA in wordlist:
		print "Checking word: " + substringA
		for word in wordlist:
			# skips checking the word against itself
			if (substringA != word) :
				print "Checking " + substringA + " against current word: " + word
				if substringA in word:
					substringB = word.replace(substringA, "")
					print "substringA: " + substringA + " exists in: " + word
					print "looking for: " + substringB
					if substringB in wordlist:
						print "EUREKA: WE HAVE SOMETHING!"
						print substringA + " " + substringB + " " + word
						specialList.append(word)
						wordlist.remove(substringA)
						wordlist.remove(substringB)
						wordlist.remove(word)

	print "The following list of words appear as substrings within the supplied dictionary: " + string.translate(str(specialList), None, "'")


main()
