import sys

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        line = line.rstrip()

        for c in line:
            if c in line[line.index(c)+1:]:
                continue
            else:
                print c
                break
        else:
            print ""


