
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

