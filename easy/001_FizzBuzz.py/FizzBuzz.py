#!/usr/bin/python

import sys
for line in open(sys.argv[1]):
  if line.rstrip() == "":
    continue
  (f, b, end)= map(lambda x: int(x), line.rstrip().split(" "))
  for num in xrange(1, end+1):
    if num % f == 0 and num % b == 0:
      print "FB",
    elif num % f == 0:
      print "F",
    elif num % b == 0:
      print "B",
    else:
      print num,
  print

