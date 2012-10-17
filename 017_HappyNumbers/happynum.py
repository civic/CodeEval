import sys

def is_happy_num(n, history=None):
   sumsq = sum([int(d)**2 for d in str(n)])
   if sumsq == 1:
       return 1
   if history == None:
       history = set()
   if sumsq in history:
       return 0 #cycle loop
   else:
       history.add(sumsq)
   return is_happy_num(sumsq, history)


with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        print is_happy_num(int(line.rstrip()))

