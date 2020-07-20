#!/usr/bin/python3
#Created by @perez_mascato

import os
from time import sleep
import pyshorteners


def banner():
    print("\033[93m--------------------------------------------")
    print("                URLCADIZ v2.0                   ")
    print("   Hide custom URL for social engineering   ")
    print("                           @perez_mascato   ")
    print("--------------------------------------------")

def programm():
    os.system('clear')
    banner()
    print("\nEx:google.com")
    original_domain = str(input("\nInput a original domain. : "))

    os.system('clear') 
    
    banner()
    print("\nInput something that: new-video-in-youtube-this-is-a-perez-mascato")
    postlink = str(input("Postlink: "))

    os.system('clear')
    
    banner()
    url_to_short = str(input("Input URL to hidde:"))
    s = pyshorteners.Shortener()
    shorten=(s.dagd.short(f'{url_to_short}'))
    withoutprotocol = shorten[8:]
    
    os.system('clear')
    banner()
    print(f"\033[95m\nYour link is: https://{original_domain}-{postlink}@{withoutprotocol}")


    defanother()
    

def defanother():
    another=str(input("\033[93m\nConvert another URL? (y/n): ")) 
    if another == "y":
        programm()

    elif another == "n":
        exit()

    else:
        print("Retry")
        sleep(3)
        os.system('clear')
        defanother()

programm()


        
