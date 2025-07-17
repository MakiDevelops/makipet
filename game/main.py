#makipet © 2025 by progman.task(MakiDevelops) is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/
import os
import glob
from time import sleep
print("Loading")

files = glob.glob('pet.goog')
for file in files:
    with open("pet.goog", "a") as f:
        f.write("newfile")
        import game