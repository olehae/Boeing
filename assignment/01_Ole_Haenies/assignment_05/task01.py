import os

macbeth_path = os.getcwd().split("\\0")[0] + r"\assignment_05_program_data\Macbeth.txt"

with open(macbeth_path) as f:
    text = f.read().splitlines()

for i in text:
    print(i)
