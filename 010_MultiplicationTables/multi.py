table = [[a * b for b in xrange(1, 13)] for a in xrange(1, 13)]
for row in table:
    print "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}".format(*row)

