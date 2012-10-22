import sys

class Stack(object):
    """my stack object"""
    def __init__(self):
        self.store = []

    def push(self, elm):
        self.store.append(elm)

    def pop(self):
        if len(self.store) == 0:
            return None

        elm = self.store[-1]
        self.store = self.store[:-1]
        return elm
    def __str__(self):
        return str(self.store)


with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        if line == "":
            intlist = []
        else:
            intlist = [int(s) for s in line.split(' ')]

        stack = Stack()
        for n in intlist:
            stack.push(n)

        out = []
        while True:
            elm = stack.pop()
            stack.pop()
            if elm != None:
                out.append(str(elm))
            else:
                break
        print " ".join(out)

                




