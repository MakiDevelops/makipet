# License
# makipet © 2025 by progman.task(MakiDevelops) is licensed under CC BY-NC-SA 4.0 https://creativecommons.org/licenses/by-nc-sa/4.0/

# Imports
import time, os, glob, f
# Vars
pet = "[o]"
hunger = 1
happy = 1


while True:
    print(f"{pet}: Hunger:{hunger} Happiness:{happy}")
    inp = input(">>")
    if inp == 'rice':
        hunger += 1
        f.clear()
    if inp == 'toy':
        happy += 1
        f.clear()
    if hunger == 6:
        print("FULL!")
        hunger = 5
        f.clear()
    if happy == 6:
        print("HAPPY!")
        happy = 5
        f.clear()