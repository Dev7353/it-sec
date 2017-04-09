import getopt, sys
import hashlib
import string, itertools

verbose = False
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "he:cl:s:bx:y:", ["help", "encrypt", "calc", "level", "length", "size", "brute force", "filea", "fileb"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    calcFlag = False
    level = 1
    length = 1

    bruteForceFlag = False
    filea = ""
    fileb = ""

    for o, a in opts:
        if o == "-h":
            printHelp()
            exit(2)
        elif o in ("-e", "--encrypt"):
            encrypt(a)
        elif o in ("-c", "--calc"):
            calcFlag = True
        elif o in ("-l", "--level"):
            level = int(a);
        elif o in ("-s", "--size"):
            length = int(a)
        elif o in ("-b", "--brute-force"):
            bruteForceFlag = True
        elif o in ("-x", "--filea"):
            filea = a
        elif o in ("-y", "--fileb"):
            fileb = a

    if calcFlag == True:
        calcCombinations(length, level)

    if bruteForceFlag == True:
        assert filea is not ""
        assert fileb is not ""
        bruteForce(filea, fileb)

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

def calcCombinations(length, level):
     alphabet_low = ""
     alphabet_high = ""
     digits = ""

     if level >= 1:
        alphabet_low += string.ascii_lowercase

     if level >= 2:
        alphabet_high += string.ascii_uppercase

     if level == 3:
        digits += string.digits

     list_of_combinations = itertools.product(alphabet_low+alphabet_high+digits, repeat=length)

     hashes = open("combinations", 'wb')
     for v in list_of_combinations:

         target = ""
         for i in range(length):
             target += v[i]

         hashes.write(target + "\n")


     hashes.close()

def bruteForce(a, b):
    target = ""
    current = ""

    fileS = open(a, 'r')
    fileD = open(b, 'r')


    srcHashes = fileS.readlines()
    srcPsw = fileD.readlines()


    for srcHash in srcHashes:
        for entry in srcPsw:
            hash = encrypt_string(entry[:len(entry)-1])

            if hash == srcHash[:len(srcHash)-1]:
                print("MATCH HASH " + hash)
                print("PASSWORD IS " + entry)
                print("")


    fileD.close()
    fileS.close()

def printHelp():

    print("-h \t --help \t \t \t Help.")
    print("-e \t --encrypt \t \t \t hash the input passwords within a file and redirect to a output file: output.")
    print("__________________________________________________")
    print("-c \t --calc \t \t \t calculate all possible passwords for given level and length.")
    print("-l \t --level \t \t \t level 1: a-z \n "
          "\t \t \t \t \t level 2: level 1 + A-Z \n "
          "\t \t \t \t \t level 3 = level 2 + 0-9")
    print("-s \t --size  \t \t \t size of the password.")
    print("__________________________________________________")
    print("-b \t --brute-force \t \t \t brute force search which requires additionally two files")
    print("-x \t --filea \t \t \t file a for brute force")
    print("-y \t --fileb \t \t \t file b for brute force")

if __name__ == "__main__":
    main()