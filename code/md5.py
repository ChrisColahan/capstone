#MD5 implementation
#reference from Applied Cryptography by Bruce Schneier

#takes a message m as imput
def MD5(in_m):
	m = list(bytearray(in_m))
	#padding
	m.append(1)
	m.append(512 - (len(in_m)+63 % 512))
	m.extend(list(bytearray(len(in_m))))
