A = input("Input a letter of the alphabet: ")

if A in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % A)
elif A == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % A) 
