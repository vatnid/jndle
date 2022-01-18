import csv, random, sys
from pprint import pprint

tsv_file = open("congkit.tsv")

read_tsv = csv.reader(tsv_file, delimiter="\t")


five_keys = []

for row in read_tsv:
    if len(row[1]) == 5:
        five_keys.append([row[0], row[2]])

#pprint(five_keys)
#print(len(five_keys))

common_chars = []
with open("test.txt", "r") as f:
    for line in f:
        line = line.strip()
        common_chars.extend(list(line))

five_common = []
for e in five_keys:
    for c in e[1]:
        if c in common_chars:
            five_common.append(e)

five_random = []
for e in five_keys:
    five_random.append(e[0])
random.shuffle(five_random)

#print(five_random)
for e in five_random:
    print(f"\"{e}\",")



