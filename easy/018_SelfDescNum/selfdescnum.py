import sys

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        digit_nums = [int(d) for d in line]
        for i, num in enumerate(digit_nums):
            findc = str(i)
            cnt = len([c for c in line if c == findc])
            if cnt != num:
                print 0
                break
        else:
            print 1 #for-loop normail ended

