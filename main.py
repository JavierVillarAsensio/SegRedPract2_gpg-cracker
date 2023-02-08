import argparse
import os
import multiprocessing
from multiprocessing import Value
import subprocess

def call_arguments():
    parser = argparse.ArgumentParser(
            description="Especifica fichero y diccionario")

    parser.add_argument('--version', action='version', 
            version='GPG Brute Force')

    parser.add_argument('--file', required=True, 
            help="Ruta del fichero a descifrar")

    parser.add_argument('--wordlist', required=True, 
            help="Ruta del diccionario a utilizar")

    return parser.parse_args()


outputfile = 'decrypted'

def gpg_brute(ifile, wordlist, part, finalizado):


    nlines = len(open(wordlist).readlines())
    nlines_part = nlines/threads
    end = nlines_part + part*nlines_part
    iter = part*nlines_part
    pos = 0

    with open(wordlist, 'r') as f:

        while pos < iter:
            f.readline()
            pos += 1

        while iter < end and not finalizado.value:
            iter += 1
            password = f.readline()
            password = password.rstrip()
                            
            resultado = subprocess.run("gpg --output {} -d --batch -q --yes --passphrase {} {}".format(outputfile, password, ifile), shell=True) 
            print("Con " + password + " resultado: ", resultado.returncode)
            if resultado.returncode == 0:
                finalizado.value = 1
                print("CONTRASEÑA ENCONTRADA: ", password)
                os._exit(1)

        
if __name__ == '__main__':
    
    args = call_arguments()
    global threads
    threads = multiprocessing.cpu_count()
    print("Numero de procesos: ",threads)
    n_p = 0

    finalizado = Value("B")
    finalizado.value = 0

    while n_p  < threads:
       p = multiprocessing.Process(target=gpg_brute, args=(args.file, args.wordlist, n_p, finalizado)).start()
       n_p += 1
    