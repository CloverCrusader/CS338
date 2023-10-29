import hashlib
import binascii
import time
import random

pStart = time.time()
# get words from file
words = [line.strip().lower() for line in open('words.txt')]
users = list()
saltDict = dict()
hashDict = dict()

# set up first dictionaries
for line in open('passwords3.txt') :
    info = line.split(':', 2) # split lines from password file by ':'
    saltNhash = info[1].split('$') # split second list member from by $ 
    users.append(info[0])
    saltDict[info[0]] = saltNhash[2]
    hashDict[info[0]] = saltNhash[3]

cracked = open('cracked3.txt', 'w')

crackd = 0
hashd = 0
while crackd < 2734:
    word = words[random.randrange(0, len(words) - 1)]
    for user in users:
        saltdWord = saltDict[user] + word
        saltdHash = binascii.hexlify(hashlib.sha256(saltdWord.encode('utf-8')).digest()).decode('utf-8')
        hashd = hashd + 1
        if saltdHash == hashDict[user]:
            users.remove(user)
            crackd = crackd + 1
            cracked.write(user + " : " + word +"\n")
            print("program has been running for", ((time.time() - pStart) * 10**3), "ms\n", hashd, "hashes computed")
cracked.close()