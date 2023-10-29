import hashlib
import binascii
import time

# create dic
# hash each word in SHA256, dic hash : word
# in loop:
    # split line by :, keep username and hash
    # lookup hash in dic, keep word
    # print username and word to file

pStart = time.time()
words = [line.strip().lower() for line in open('words.txt')]

hashDict = dict()

# fill dictionary
start = time.time()
for word in words:
    hashd = binascii.hexlify(hashlib.sha256(word.encode('utf-8')).digest()).decode('utf-8')
    hashDict[hashd] = word
stop = time.time()
print("pre-hashing took " , ((stop - start) * 10**3) , "ms\n")


# open file to write to
crackd = open('pCrack1.txt', 'w')

# go through password hash file line by line
start = time.time()
for line in open('passwords1.txt') :
    info = line.split(':', 2)
    crackd.write(info[0] + ' : ' + hashDict[info[1]]+ "\n")
stop = time.time()
print("hash matching took " , ((stop - start) * 10**3) , "ms\n")
crackd.close()

pEnd = time.time()
print("program ran for " , ((pEnd - pStart) * 10**3) , "ms\n")
# in loop:
    # split line by :, keep username and hash
    # lookup hash in dic, keep word
    # print username and word to file
