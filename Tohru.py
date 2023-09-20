#!/usr/bin/python3

import crypt
import sys
import os

os.system("clear")
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

                # Format wordlist
                wordlist = sys.argv[1]
                os.system(f"sed '/^$/d' {wordlist} > clear_wordlist.txt")

                # Opening and reading Wordlist

                try:
                        with open('clear_wordlist.txt','r', encoding='iso8859_15') as file:
                                while (line := file.readline().rstrip()):

                                        hashsalt = crypt.crypt(line,salt)

                                        if show == "Y":
                                        # if hash match
                                                if hashsalt == hash:
                                                        print(f"\033[31m[HASH]:\033[m {hashsalt} \033[31m\n[SENHA]:\033[m {line}")
                                                        exit()
                                                        os.system(f"rm clear_wordlist.txt")
                                        elif show == "N":
                                                print(f"{line} - {hashsalt}\n")

                                                if hashsalt == hash:
                                                        print(f"\033[31m[HASH]:\033[m {hashsalt} \033[31m\n[SENHA]:\033[m {line}")
                                                        exit()
                                                        os.system(f"rm clear_wordlist.txt")


                except Exception as error:
                        print(f"\033[31m[*] Wordlist didn't load\n[*] {error}")
                        exit()

        except Exception as error:
                print(f"\033[31m[*] Module not installed\n[*] {error}")
                print(f"\033[32m[+] Module art installed run script again!")
                os.system("pip3 install art > /dev/null 2>&1")
                exit()
