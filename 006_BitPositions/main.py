import sys
for line in open(sys.argv[1]):
  if line.rstrip() == "":
    continue
  (x, p1, p2) = map(lambda y: int(y), line.rstrip().split(","))
  str_bin = bin(x)
  print str((str_bin[-p1] == str_bin[-p2])).lower()
    
