import hashlib
import binascii
import time
import random

pStart = time.time()
# get words from file
words = [line.strip().lower() for line in open('words.txt')]
infoDict = dict()
for line in open('passwords2.txt') :
    info = line.split(':', 2)
    infoDict[info[1]] = info[0]

# generate random pair, hash, and check if it's a password
crackd = 0
hashd = 0
while crackd < 2734:
    pair = words[random.randrange(0, len(words) - 1)] + words[random.randrange(0, len(words) - 1)]
    pairHash = binascii.hexlify(hashlib.sha256(pair.encode('utf-8')).digest()).decode('utf-8')
    hashd = hashd + 1
    entry = infoDict.get(pairHash, "none")
    if entry != 'none':
        crackd = crackd + 1
        print(entry + ' : ' + pair + "\n")
        print("program has been running for" , ((time.time() - pStart) * 10**3) , "ms\n")
        print(hashd, "hashes computed")
