#Libraries
import random
import sys
import hashlib
from operator import xor
#from Crypto.PublicKey import RSA
import calendar
import time
communi = 0
storage = 0
logint = 0
regt = 0
thash = 0
tkey = 0
print("Enter Username...")
ID = str(input()).encode()
print("Enter Password...")
PW = str(input()).encode()
c = random.randint(1, 10000)
b = random.randint(1, 10000)
a = bin(abs(b - c))[2:].encode()
h1start = time.time()
CPW = (hashlib.sha3_256(ID + PW + a)).hexdigest()
#communi = sys.getsizeof(CPW) + sys.getsizeof(ID)
#print("Size Of MPW:", sys.getsizeof(CPW))
h1end = time.time()
thash = h1end - h1start
string ="shafiq"
string2 = "ahmed"
tcon = time.time()
string3 = string+string2
tconend = time.time()
tcontotal = tconend-tcon
txor = time.time()
temp = xor(bool(a),bool(b))
txorend = time.time()
txortotal = txorend-txor
tmul = time.time()
tempp = 382**379
tempppp=tempp*tempp
tmulend = time.time()
ttotal = tmulend-tmul
print("time of point multiplication", (ttotal/1000))
print("time of XOR : ", (txortotal/1000))
print("Time of concatenation : ", (tcontotal/1000))
print("Time of hash function : ", (thash/1000))