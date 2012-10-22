import sys

with open(sys.argv[1], "r") as f:
    allchar = set([chr(c) for c in xrange(ord('a'), ord('z')+1)]) #all alpha chars

    for line in f.readlines():
        line = line.rstrip()
        diff = allchar.difference(set(line.replace(" ", "").lower()))
        if len(diff) == 0:
            print 'NULL'
        else:
            print "".join(sorted(diff))

