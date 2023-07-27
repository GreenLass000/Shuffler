import os
import random

path = r""
filetype = ""

names = os.listdir(path)
shuffled = names.copy()

random.shuffle(shuffled)

for i, n in enumerate(names):
    os.rename(f"{path}\\{n}", f"{path}\\{i}.{filetype}")

for i, n in zip(os.listdir(path), shuffled):
    os.rename(f"{path}\\{i}", f"{path}\\{n}")
