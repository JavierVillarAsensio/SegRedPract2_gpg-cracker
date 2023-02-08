import itertools


def wordlist_generator(wordlist):
    chrs='abcdefghijklmnñopqrstuvwxyz'

    n = int(input("Introduce the lenght of the maximum length word of the wordlist: \n")) 

    file = open(wordlist, "w")

    for i in range(1,n+1):
      for xs in itertools.product(chrs, repeat=i):
        file.write((''.join(xs)) + "\n")

    file.close()


wordlist_generator("wordlist.txt")
