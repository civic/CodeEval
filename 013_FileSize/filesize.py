import sys

size = 0
with open(sys.argv[1], "rb") as f:
    for b in f.read():
        size += 1
print size
