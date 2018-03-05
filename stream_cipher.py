import binascii
import keydHash

def user_text():
  plaintext = "hahaha lol"
  print ("plaintText is :")
  print plaintext
  string_to_binary(plaintext)

def string_to_binary(user_text):
  binary_list = [ bin(ord(ch))[2:].zfill(8) for ch in user_text ] #in list form
  encryption_box(binary_list)

def encryption_box(binary_list):
  key = "01101011"
  ct_blist = []
  ct_dec = []
  ct = []
  for i in range(len(binary_list)):
    xor_key_blist = int(binary_list[i], 2)^int(key, 2) #xored
    encrypting = bin(xor_key_blist)[2:].zfill(len(binary_list[1]))    #xored encryption
    ct_blist.append(encrypting)
    ct_dec.append(int(ct_blist[i], 2))
    ct.append(chr(ct_dec[i]))
  print("cipher text : ")
  import pdb;pdb.set_trace()
  print ct

user_text()

