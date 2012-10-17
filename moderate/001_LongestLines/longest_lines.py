import sys

with open(sys.argv[1], "r") as f:
    topN = int(f.readline().rstrip())
    print "".join(sorted(f.readlines(), lambda a,b: cmp(len(b), len(a)))[:topN]),

