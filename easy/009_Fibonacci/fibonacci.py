
import sys

cache = {0: 0, 1: 1}
def fib(n):
    if cache.has_key(n):
        return cache[n]
    n2 = fib(n - 2)
    n1 = fib(n - 1)
    cache[n] = n1 + n2
    return cache[n]

with open(sys.argv[1], "r") as f:
    for line in f:
        n = int(line.rstrip())
        print fib(n)

