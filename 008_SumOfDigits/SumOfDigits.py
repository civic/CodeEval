import sys
with open(sys.argv[1], "r") as f:
    for line in f:
        sum = reduce(lambda s1, s2:int(s1) + int(s2), line.rstrip())
        print sum

