import sys

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        s, t = line.rstrip().split(",")
        # using rfind
        #print s.rfind(t)

        # dont use rfind
        for i, c in enumerate(reversed(s)):
            if c == t:
                print len(s) - i - 1
                break
        else:
            print -1
            
