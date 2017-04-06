
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

#utility function to check if char is alpha
def isalpha(char):
	val = ord(char)
	return (val >= ord('a') and val <= ord('z')) or (val >= ord('A') and val <= ord('Z'))

#utility function to convert alpha 
#ASCII character to int in range [0,26] inclusive
def ascii2modchar(char):
	if not isalpha(char):
		raise Exception('Given character is not alpha')
	val = ord(char.upper()) - ord('A')
	return val

#utility function to convert int in range [0,26]
#to a charcter in the range ['A','Z']
def modchar2ascii(val):
	return chr((val % 26) + ord('A'))

#char should be an alphabetic char (i.e. in the range ['A','Z'])
#shift should be an alphabetic character.
#A shifts by zero.
def encode(char, shift):
	#transform the chararcter into the 0-25 range
	#if it is alpha
	val = ascii2modchar(char)
	shift_val = ascii2modchar(shift)
	
	#E(p,k)= (p+k) (mod 26)
	return modchar2ascii((val + shift_val) % 26)

#encodes a string
def encode_str(string, key):
	out = ""
	keystr = ""
	out2 = ""
	for char in key:
		if isalpha(char):
			keystr += char
	if len(keystr) is 0:
		raise Exception('no alpha characters in the key')
	for char in string:
		if isalpha(char):
			out += char
	for i in range(len(out)):
		out2 += encode(out[i], keystr[i % len(keystr)])
	return out2

#char is a ciphertext character to be decoded
#shift is the corresponding key character
def decode(char, shift):
	#convert character to [0,25]
	val = ascii2modchar(char)
	shift_val = ascii2modchar(shift)
	
	#D(c,k)=(26+c-k) (mod 26)
	return modchar2ascii((26 + val - shift_val) % 26)

#decodes a string
def decode_str(string, key):
	out = ""
	out2 = ""
	keystr = ""
	for char in key:
		print(char)
		if isalpha(char):
			keystr += char
	if len(keystr) is 0:
		raise Exception('no alpha characters in the key')
	for char in string:
		if isalpha(char):
			out += char
	for i in range(len(out)):
		out2 += decode(out[i], keystr[i % len(keystr)])
	return out2

#returns an array of frequencies of the characters in a string
#the first position is 'A', the second 'B', and so on. The array is 26 long
#the elements in the table are in teh range [0,1]
def freq(string):
	freq_table = [0] * 26
	numchars = 0
	for char in string:
		if isalpha(char):
			val = ascii2modchar(char)
			freq_table[val] += 1
			numchars += 1
	for i in range(26):
		freq_table[i] /= numchars
	return freq_table

#caluclate error for a shift
def find_err(standard_freq_table, cipher_freq_table, shift):
	#calculate avg freq difference from shifted tables
	err = 0
	for i in range(1,26):
		#calculate least squares difference
		err += (standard_freq_table[i] - cipher_freq_table[(i + shift) % 26])**2
	return err
#frequency analysis for vigenere cipher
def find_key(ciphertext, standard_freq_table):
	#first, find the length of the key
	#start by assuming a length of 1 character
	key_len = 1
	min_len = 1
	min_err = 100
	#test all key lengths 1 through len(ciphertext).
	#if the length of the key is the same as the length of the ciphertext, then it could be a one-time-pad and we wont be able to find the key
	#set a hard limit. otherwise frequency analysis will not work on offsets close to the length of the ciphertext
	while key_len < len(ciphertext) and len(ciphertext) // key_len > 100:
		#collect all n*i elements. they would all be encoded using the same character in the key.
		first_cipher_char = ""
		j = 0
		while key_len * j < len(ciphertext):
			first_cipher_char += ciphertext[key_len * j]
			j += 1
		#next, perform frequency analysis to determine if there this is probably the correct key length
		for k in range(26):
			err = find_err(standard_freq_table, freq(first_cipher_char), k)
			#heuristic used here to remove multiples of smallest key, since it would be the same key repeated. But a large jump also signifies that the key is more likely to be correct.
			if err < min_err and (key_len % min_len is not 0 or min_err / 2 > err):
				min_err = err
				min_len = key_len
				print(err)
				print("new min length:" + str(min_len))
		key_len += 1
	
	#now that the key lenth is known, the key can be obtained by breaking each of the key characters
	key = ""
	for key_i in range(min_len):
		#get all charcters encoded using the same character
		cipher_chars = ""
		j = 0
		while (min_len*j)+key_i < len(ciphertext):
			cipher_chars += ciphertext[(min_len*j)+key_i]
			j += 1
		#find the least error. that is probably the shift
		least_err = 100
		least_shift = 0
		for i in range(26):
			err = find_err(standard_freq_table, cipher_chars, i)
			if err < least_err:
				least_err = err
				least_shift = i
		#add the new key character to the key string
		key += modchar2ascii(least_shift)
		print("found new charcter in key: " + modchar2ascii(least_shift))
	return key

#from huckelberry fin text from http://www.gutenberg.org/ebooks/76
string = open('huckelberryfinn.txt').read()
key = "MYSUPERSECRETKEY"

#print(string)
#print("\n\n\n")
encoded = encode_str(string, key)
print(encoded)
print("\n\n\n")
decoded = decode_str(encoded, key)
print(decoded)
print("\n\n\n")
print(find_key(encoded, standard_freq_table))

