import sys

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        # using intersection method.
        # a, b = [set(x.split(",")) for x in line.rstrip().split(";")]
        # print ",".join(sorted(a.intersection(b)))
        
        a, b = [[int(s) for s in x.split(",")] for x in line.rstrip().split(";")]
        inter = []
        for x in a:
            for y in b:
                if x == y:
                    inter.append(str(x))
                    break
                elif x < y:
                    break;
                elif x > y:
                    continue;
        print ",".join(inter)


