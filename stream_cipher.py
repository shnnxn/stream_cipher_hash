from operator import xor
import binascii

def string_to_binary():
  st = "hello world"
  key = "10101010"
  er = [ bin(ord(ch))[2:].zfill(8) for ch in st ] #in list form
  pt = ' '.join(format(ord(x), 'b') for x in st)    # not in list form
  z = int(er[1], 2)^int(key, 2)
  enc = bin(z)[2:].zfill(len(er[1]))
  return enc

print (string_to_binary())
