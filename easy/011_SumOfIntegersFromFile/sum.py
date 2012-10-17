import sys

with open(sys.argv[1], "r") as f:
    print reduce(lambda a,b:a+b, [int(s.rstrip()) for s in f])
