for num in range(1000, 1, -1):
  prime = True
  for div in range(2, num - 1):
    if num % div == 0:
      prime = False
      break
  if prime:
    str_num = str(num)
    palindrome = True
    len_num = len(str_num)
    for i in range(int(len_num/2)):
      if str_num[i] != str_num[-(i+1)]:
        palindrome = False
        break

    if palindrome:
      print str_num
      break


