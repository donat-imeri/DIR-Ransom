
import os, random, io
import string
from Crypto.PublicKey import RSA


key = RSA.generate(2048) #generate pub and priv key
f = open ('publicANDprivate.txt', 'w')
f.write(str(key.exportKey()))
f.close()

print(key.exportKey())

