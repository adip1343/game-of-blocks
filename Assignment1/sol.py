from time import time
from hashlib import sha256
import random

random.seed(time())

target  = 0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
big_num = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
s = input()

a = sha256()
i = 0
start = time()

print("Initial hash of our string is : {}".format(a.hexdigest()))

while True :
    random_number = str(random.randrange(big_num))
    inp = s + random_number
    i += 1
    a.update(inp.encode('ascii'))
    if int(a.hexdigest(),16) <= target :
        print("Hash of new string is : {}".format(a.hexdigest()))
        print("New string is : {}".format(inp))
        print("It took {} iterations.".format(i))
        break

print("Time taken is {}".format(time()-start))