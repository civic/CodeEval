import sys
for line in open(sys.argv[1]):
  if line.rstrip() == "":
    continue
  words = line.rstrip().split(" ")
  words.reverse()
  print " ".join(words)
  
