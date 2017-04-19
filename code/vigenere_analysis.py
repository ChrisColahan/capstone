
#caluclate error for a shift of the tables
def find_err(cipher_freq_table, shift):
        #calculate avg freq difference from shifted tables
        err = 0
        for i in range(0,26):
		#calculate chi-squared
                standard_freq = standard_freq_table[i]
                cipher_freq = cipher_freq_table[(i + shift) % 26]
                cipher_err = (standard_freq - cipher_freq) ** 2
                cipher_err /= standard_freq
                err += cipher_err
        return err/26

#frequency analysis for vigenere cipher
def find_key(ciphertext, standard_freq_table):
        #first, find the length of the key
        #start by assuming a length of 1 character
        key_len = 1
        min_len = 1
        min_err = 1
        cipher_len = len(ciphertext)
        min_freq_len = 100
        
        #test all key lengths 1 through len(ciphertext).
        #if the length of the key is the same as the length of
        #the ciphertext, then it could be a one-time-pad and we
        #wont be able to find the key set a hard limit. Otherwise
        #frequency analysis will not work on offsets close to the
        #length of the ciphertext
        while key_len < cipher_len and cipher_len // key_len > min_freq_len:
                #collect all n*i elements. they would all be
                #encoded using the same character in the key.
                first_cipher_char = ""
                j = 0
                while key_len * j < len(ciphertext):
                        first_cipher_char += ciphertext[key_len * j]
                        j += 1
                #next, perform frequency analysis to determine if
                #there this is probably the correct key length
                for k in range(26):
                        err = find_err(freq(first_cipher_char), k)
                        #heuristic used here to remove multiples of
                        #smallest key, since it would be the same
                        #key repeated. But a large jump also could
                        #also signify that the key is more likely
                        #to be correct.
                        multiple = key_len % min_len is 0
                        large_jump = min_err / 2 > err
                        if err < min_err and (not multiple or largejump):
                                min_err = err
                                min_len = key_len
                key_len += 1
        
        #now that the key lenth is known, the key can be obtained by
        #performing frequency analysis on each of the key characters
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
                        err = find_err(freq(cipher_chars), i)
                        if err < least_err:
                                least_err = err
                                least_shift = i
                #add the new key character to the key string
                key += modchar2ascii(least_shift)
        return key

