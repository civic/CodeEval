import sys
for line in open(sys.argv[1]):
  if line.rstrip() == "":
    continue
  print line.rstrip().lower()
    
  
