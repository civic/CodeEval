import sys
for line in open(sys.argv[1]):
  if line.rstrip() == "":
    continue
  (x, n) = map(lambda y: int(y), line.rstrip().split(","))
  while n < x:
    n *= 2
  print n
  
