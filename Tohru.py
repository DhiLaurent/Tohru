#!/usr/bin/python3

import crypt
import sys


def banner():
        print("\033[31m---------------------------------------------------")
        tprint(" Tohru ",font="slant")
        print("----------------------------------------------------\033[m")


if len(sys.argv) != 2:
        # Infos
        print("\033[31m+--------------------------------------------------------+")
        print("|       Como usar: python3 Tohru.py (WordList)           |")
        print("|        How to use: python3 Tohru (Wordlist)            |")
        print("+--------------------------------------------------------+\033[m")

elif len(sys.argv) == 2:
        try:
                from art import *
                # Banner
                banner()
                # Full Hash
                hash = input("\033[31mHash Completa:\033[m ")
                # Salt
                salt = input("\033[31mSalt:\033[m ")
                show = input("WordList Oculta/Hide WordList (Y/N) ?").upper()
                print("\n")
                print("\033[31m                 +--------------------------------------------+")
                print("                 |        Cracking hold a second...           |")
                print("                 +--------------------------------------------+\033[m")
                print("\n")
                # Opening and reading Wordlist

                try:
                        with open(sys.argv[1],'r', encoding='iso8859_15') as file:
                                while (line := file.readline().rstrip()):
                                        hashsalt = crypt.crypt(line,salt)

                                        if show == "Y":
                                        # if hash match
                                                if hashsalt == hash:
                                                        print(f"\033[31m[HASH]:\033[m {hashsalt} \033[31m\n[SENHA]:\033[m {line}")
                                                        exit()
                                        elif show == "N":
                                                print(f"{line} - {hashsalt}\n")

                                                if hashsalt == hash:
                                                        print(f"\033[31m[HASH]:\033[m {hashsalt} \033[31m\n[SENHA]:\033[m {line}")
                                                        exit()

                except Exception as error:
                        print("\033[31m[*] Wordlist didn't load")
                        print(error)
                        exit()

        except Exception as error:
                print("\033[31m[*] Module not installed")
                print(error)
                exit()
print("\033[31m------------------------------------------------------------------------------\n")
print("                 +--------------------------------------------+")
print("                 |      Tohru couldn't break the hash :c      |")
print("                         |        Try to change WordList              |")
print("                 +--------------------------------------------+\n")
print("\033[31m------------------------------------------------------------------------------")
