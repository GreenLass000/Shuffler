import os
import random

path = r"C:\Users\marco\Documents\test"

names = os.listdir(path)
shuffled = names.copy()

random.shuffle(shuffled)

for i, n in enumerate(names):
    os.rename(f"{path}\\{n}", f"{path}\\{i}.png")

for i, n in zip(os.listdir(path), shuffled):
    os.rename(f"{path}\\{i}", f"{path}\\{n}")
