#returns an array of frequencies of the characters in a string
#the first position is 'A', the second 'B', and so on. The array is 26 long
#the elements in the table are in teh range [0,1]
def freq(string):
	freq_table = [0] * 26
	numchars = 0
	for char in string:
		if char.isalpha():
			val = ascii2modchar(char)
			freq_table[val] += 1
			numchars += 1
	for i in range(26):
		freq_table[i] /= numchars
	return freq_table
