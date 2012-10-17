import sys

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        print ",".join(sorted(list(set(line.split(",")))))
        
