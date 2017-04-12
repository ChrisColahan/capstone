#find the sift of an ecoded string.
#the idea is to try all shifts (0,1,2,...25)
#and to determine which one is the least difference between
#the standard frequency table and the generated one 
#from the ciphertext.
def find_shift(cipher_freq_table):
        min_shift = 0
        min_err = 1
        # try all shifts
        for i in range(0,26):
                #calculate avg freq difference from shifted tables
                err = 0
                for j in range(0,26):
                        #calculate least squares difference
                        standard_freq = standard_freq_table[j]
                        cipher_freq = cipher_freq_table[(j + i) % 26]
                        err += (standard_freq - cipher_freq) ** 2
                err /= 26
                if(err < min_err):
                        min_err = err
                        min_shift = i
        return min_shift
