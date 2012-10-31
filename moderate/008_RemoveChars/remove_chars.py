import sys

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        statement, chars = line.rstrip().split(",")
        chars = chars.strip()
        for c in chars:
            statement = statement.replace(c, "")
        print statement
