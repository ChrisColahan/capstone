
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
def encode_str(string, key):
	out = ""
	keystr = ""
	for char in key:
		if isalpha(char):
			keystr += char
	if len(keystr) is 0:
		raise Exception('no alpha characters in the key')
	for char in string:
		if isalpha(char):
			out += char
	for i in range(len(out)):
		out += encode(out[i], ascii2modchar(keystr[i % len(keystr)]))
	return out

#decodes a string
def decode_str(string, key):
	out = ""
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
		out += encode(out[i], (26 - ascii2modchar(keystr[i % len(keystr)])) % 26)
	return out

#from huckelberry fin text from http://www.gutenberg.org/ebooks/76
string = open('huckelberryfinn.txt').read()
key = "MYSUPERSECRETKEY"

print(string)
print("\n\n\n")
encoded = encode_str(string, key)
print(encoded)
print("\n\n\n")
decoded = decode_str(encoded, key)
print(decoded)

