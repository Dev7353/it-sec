import getopt, sys
import hashlib
import string, itertools

verbose = False
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:b:c:l:v", ["hash", "brute-force", "calc", "length"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    length = 1
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--hash"):
            encrypt(a)
        elif o in ("-l", "--length"):
            length = int(a)
        elif o in ("-c", "--calc"):
            calcCombinations(length, a)
        elif o in ("-b", "--brute-force"):
            bruteForce(a)


def encrypt(a):
    if verbose == True:
        print("Hash File input with SHA1 algorithm.")

    output = open("output", 'wb')
    pws = open(a, 'r')
    l = pws.readlines()

    for line in l:
        output.write(encrypt_string(line[:len(line)-1]))
        output.write("\n")
    output.close()
    pws.close()

def encrypt_string(string):

    hash = hashlib.sha1()
    hash.update(string)
    return hash.hexdigest()

def calcCombinations(length, file):
     alphabet_low =  string.ascii_lowercase
     alphabet_high = string.ascii_uppercase
     digits = string.digits

     list_of_combinations = itertools.product(alphabet_low+alphabet_high+digits, repeat=length)
     hashes = open(file, 'a')
     for v in list_of_combinations:

         target = ""
         for i in range(length):
             target += v[i]

         hashes.write(target + "|" + encrypt_string(target) + "\n")


     hashes.close()

def bruteForce(a, b):
    target = ""
    current = ""



if __name__ == "__main__":
    main()