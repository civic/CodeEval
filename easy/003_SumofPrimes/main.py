sum_of_primes = []
num = 2
while(len(sum_of_primes) < 1000):
  prime = True
  for div in range(2, num - 1):
    if num % div == 0:
      prime = False
      break
  if prime:
    sum_of_primes.append(num)
  num += 1


print reduce(lambda x,y: x+y, sum_of_primes)


