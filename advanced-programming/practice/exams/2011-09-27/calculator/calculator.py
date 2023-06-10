from operator import *
from queue import *

operations = {"+":add,
              "-":sub,
              "*":mul,
              "/":truediv} 

class calculator():
    def __init__(self, polish):
        self.polish = polish

    def eval(self): # +2*-53/63 ((6/3)*(5-3))+2
        stack = []
        def inner(s):
            if len(s) == 0:
                return stack[0]
            if s[0] not in operations.keys(): # digit
                stack.append(int(s[0]))
            else:
                stack.append(operations[s[0]](stack.pop(), stack.pop()))
            return inner(s[1:])
        return inner(list(reversed(self.polish)))

    def code(self):
        string = ""
        stack = []
        c = 0
        def inner(s):
            nonlocal string, c 
            if len(s) == 0:
                string += ''.join([f"{operations[i].__name__}\n" for i in stack[::-1]])
                return string
            if s[0] not in operations.keys():
                string += f"store {s[0]}\n"
                c += 1
            else:
                c = 0
                stack.append(s[0])
            if c == 2:
                string += f"{operations[stack.pop()].__name__}\n"
    
            return inner(s[1:])
        return inner(list(self.polish))
