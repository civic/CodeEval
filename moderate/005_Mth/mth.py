import sys

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        splitted = line.split(' ')
        chars, idx = splitted[:-1], int(splitted[-1])
        if len(chars) < idx:
            print 
        else:
            print chars[-idx]


