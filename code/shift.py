
#utility function to convert alpha 
#ASCII character to int in range [0,26] inclusive
def ascii2modchar(char):
	if not char.isalpha():
		raise Exception('Given character is not alpha')
	val = ord(char.upper()) - ord('A')
	return val

#utility function to convert int in range [0,26]
#to a charcter in the range ['A','Z']
def modchar2ascii(val):
	return chr((val % 26) + ord('A'))

#char should be an alphabetic char (i.e. in the range ['A','Z'])
#shift should be in the range [1,25]. 
#0 wouldn't shift at all and 26 shifts a full rotation, so essentially 0.
def encode(char, shift):
	#transform the chararcter into the 0-25 range
	#if it is alpha
	val = ascii2modchar(char)
	
	#check to see that the character is alpha
	if val >= 0 and val < 26:
		#E(p,k)= (p+k) (mod 26)
		val = (val + shift) % 26

		#convert the number back to ASCII
		#and return it as a char
		return modchar2ascii(val)
	else:
		raise Exception('the character was not alpha')

#encodes a string
def encode_str(string, shift):
	out = ""
	for char in string:
		if char.isalpha():
			out += encode(char, shift)
	return out

#decodes a string
def decode_str(string, shift):
	#since the decode can be done using the inverse of the shift
	#(i.e. some n such that (shift+n)(mod26) = 0)
	#that is what happens here
	return encode_str(string, 26-shift)

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

#find the sift of an ecoded string.
#the idea is to try all shifts (0,1,2,...25)
#and to determine which one is the least difference between
#the standard frequency table and the generated one 
#from the ciphertext.
def find_shift(standard_freq_table, cipher_freq_table):
	min_shift = [[0,1]]
	# try all shifts
	for i in range(0,26):
		#calculate avg freq difference from shifted tables
		err = 0
		for j in range(0,26):
			#calculate chi-squared
			err += ((cipher_freq_table[(j + i) % 26] - standard_freq_table[j])**2) / standard_freq_table[j]
		min_shift.append([i, err/26])
	return list(map(lambda x: x[0], sorted(min_shift, key=lambda x: x[1])))

#table from paper (The code book, Singh)
standard_freq_table = [
	0.082,#A
	0.015,#B
	0.028,#C
	0.043,#D
	0.127,#E
	0.022,#F
	0.02,#G
	0.061,#H
	0.07,#I
	0.002,#J
	0.008,#K
	0.04,#L
	0.024,#M
	0.067,#N
	0.075,#O
	0.019,#P
	0.001,#Q
	0.06,#R
	0.063,#S
	0.091,#T
	0.028,#U
	0.01,#V
	0.024,#W
	0.002,#X
	0.02,#Y
	0.001#Z
]

#from huckelberry fin text from http://www.gutenberg.org/ebooks/76
string = open('huckelberryfinn.txt', encoding='utf-8').read()
key = 12

encoded = encode_str(string, key)
freq_table = freq(encoded)
print("frequency table:")
for i in range(26):
	print(modchar2ascii(i) + " : " + "{0:.3f}".format(freq_table[i]) + "%")
print(find_shift(standard_freq_table, freq_table))

