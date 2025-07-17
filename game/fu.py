import os, platform

def clear():
    if platform == "darwin":
        os.system('clear')
    else:
        os.system('cls')