import sys


with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        nums = line.rstrip().split(" ")
        for i,s in enumerate(nums[:-1]):
            try:
                # 2 0 6 3 1 6 3 1 6 3 1
                #     ^     ^
                #     i    sidx
                #     ---3---    length

                sidx = nums.index(s, i+1)   # start index
                length =  sidx - i          # logest length
                for j,s2 in enumerate(nums[i:sidx]):
                    if s2 != nums[sidx+j]:
                        length = j
                        break
                print " ".join(nums[sidx:sidx + length])
                break
            except ValueError, e:
                continue
        else:
            sidx = -1

