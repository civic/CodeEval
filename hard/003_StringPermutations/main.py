import sys

result = None
def main():
  global result
  for line in open(sys.argv[1]):
    if line.rstrip() == "":
      continue

    result = set()
    word = line.rstrip()

    word_chars = list(word)
    recur(word_chars, "")
    print ",".join(list(sorted(result)))

def recur(chars, str):
  if len(chars) > 1:
    for (i, c) in enumerate(chars):
      newstr = str + c
      newchars = chars[:]
      newchars.pop(i)
      recur(newchars, newstr)
  else:
    str += chars[0]
    result.add(str)

main()
