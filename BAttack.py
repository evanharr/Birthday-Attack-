import hashlib
import string
import random



def string_to_bytes(string_value):
    return bytearray(string_value,
                     encoding='utf-8')
def write_bytes(fn, message,hash):
    f = open(fn, "wb")
    f.write(message + '|' + hash)
    f.close()

def write_file(fn, hash,message):
    f = open(fn, "w")
    f.write(hash + '\t' +message + '\n')
    f.close()

def read_file(fn):
    f = open(fn)


def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()

    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def bit_to_hex(str):
    str = str.hex()
    return str

x = hashlib.sha256()


def BadHash40(s):

    #creates sha256 object
    fullHash = hashlib.sha256()
    #updates hash with entered string
    fullHash.update(s)
    fullHashText = fullHash.hexdigest()
    # 4 bits = 1 hex digit
    # first 40 bits = 10 hex digit
    BadHash = fullHashText[:10]

    return BadHash



def random_stringGen():
    #returns string with upper and lower case letters
    letters = string.ascii_letters
    #returns string with numbers
    digits = string.digits
    #returns string with punctuation
    punctuation = string.punctuation
    #create string of letters,numbers,punctuation
    randMess = letters+digits+punctuation
    #create random message of 256 characters
    message = ''.join(random.choice(randMess) for i in range(256))
    #turn message into bits
    #print(len(message))
    message = string_to_bytes(message)
    #message = message.encode('utf-8')
    return message




dictHash = {}
dictMessage = {}
dictTest = {}
i = 0

for i in range(0,1048576):
    message = random_stringGen()

    hash40 = BadHash40(message)

    message = message.hex()
    dictMessage[i] = (message, hash40)
    dictHash[i] = hash40
    dictTest[i] = (hash40,message)







print("finished hashing \n")
print("dictHash length",len(dictHash.keys()))
dictHashSorted = (sorted(dictHash.values()))
dictTestSorted = (sorted(dictTest.values()))

print("dictHashSorted length",len(dictHashSorted))

print("finished sorting \n")
no_collision = 0
for k in dictTestSorted:
    try:
        next =(dictTestSorted.index(k) +1)
        next = dictTestSorted[next]
    except(ValueError, IndexError):
        next = 0
    print("index: ", dictTestSorted.index(k))
    print("k: ", k[0])
    print("next: ", next[0])


    if k[0] == next[0]:
        print("message & hex 1: ", k)
        print("message & hex 2: ", next)

        for k in dictTestSorted:
            write_file("Birthday Attack.txt", k[0], k[1])

        exit()
