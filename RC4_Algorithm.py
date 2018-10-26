#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:14:23 2018

@author: Fancy Wu 

"""

def main():
    ##M means Plaintext
#    M = ["S", "h", "e", "n", "z", "h", "e", "n", " ", 
#            "U", "n", "i", "v", "e", "r", "s", "i", "t", "y"]
    
    M = list(raw_input("Enter Plaintext please:"))
    key = list(raw_input("Enter key please:"))
    mv_len = len(M)
    
    print "\nResult:\n(1)"
    ##Generate keyStream
    key_str = Generate_key_Stream(init(key), mv_len)
    
    print "Plaintext  : " + str(CombineList(M))
    
    ##C means Ciphertext
    ##encryption for plaintext
    M = char2int(M,mv_len)

    C = [0 for i in range(mv_len)]
    C_char = [0 for i in range(mv_len)]
    for i in range(mv_len):
        ##save each number
        C[i] = M[i] ^ key_str[i]
        ##transfer int into char
        C_char[i] = chr(C[i])
    
    ##print result
    print "Ciphertext : " + str(C_char)
    print "length of Plaintext : " + str(mv_len)
    print "length of Ciphertext : " + str(len(C_char))
    print "(2)"
    print "Plaintext:  " + str(M)
    print "Keystream:  " + str(key_str)
    print "Ciphertext: " + str(C)
    M_content, KS_content, C_content  = Save_As_Binary(M,key_str,C,mv_len)
    print "(3)"
    print "Plaintext:  " + str(M_content)
    print "Keystream:  " + str(KS_content)
    print "Ciphertext: " + str(C_content)
    
    ###################################################################
    ##validation
    M_valid = [0 for i in range(mv_len)]
    for i in range(mv_len):
        M_valid[i] = C[i] ^ key_str[i]
        M_valid[i] = chr(M_valid[i])
    print "(4)Validation"
    print "Plaintext  :" + str(C_char)
    print "Ciphertext :" + str(CombineList(M_valid))
        
      
##initialization
def init(key):
    ##transfer char into number 
    print "key : " + str(CombineList(key))
    
    key = char2int(key,len(key))
    s = [0 for i in range(256)]
    k = [0 for i in range(256)]
    for i in range(256):
        s[i] = i
        k[i] = key[i%5]

    j = 0
    temp = 0
    for i in range(256):
        j = (j + s[i] + k[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    return s


##Generate keystream
def Generate_key_Stream(s, mv_length):
    j, t= 0, 0
    temp = 0
    key_stream = [0 for i in range(mv_length)]
    for i in range(mv_length):
        j = (j + s[i+1]) % 256
        temp = s[i+1]
        s[i+1] = s[j]
        s[j] = temp
        t = (s[i+1] + s[j]) % 256
        key_stream[i] = s[t]
    return key_stream


##save M,key_str and C as binary
def Save_As_Binary(m,ks,c,mv_len):
    M, KS, C = [], [], []
    for i in range(mv_len):
        M.append('{:08b}'.format(m[i]))
        KS.append('{:08b}'.format(ks[i]))
        C.append('{:08b}'.format(c[i]))
    M_content = CombineList(M)
    KS_content = CombineList(KS)
    C_content = CombineList(C)
    return M_content, KS_content, C_content


##transfer char into int
def char2int(m, m_len):
    for i in range(m_len):
        m[i] = ord(m[i])
    return m

##combine sequence in list
def CombineList(l):
    l_content = " ".join(l)
    return l_content


if __name__ == '__main__':
    main()

        


    
    
    






















