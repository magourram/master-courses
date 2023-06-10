class Node(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

class calculator(object):
    def __init__(self, expr):
        self.root = Node(expr[0])
        self.expr = expr
        self.build_tree(expr[1:])

    def build_tree(self, my_string):
        current = self.root
        my_s = my_string
        index = 0

        def inner(current):
            nonlocal index
            nonlocal my_s
        
            if index == len(my_s):
                return 

            current.l = Node(my_s[index])
            index += 1
            if not my_s[index-1].isdigit():
                inner(current.l) 
            
            current.r = Node(my_s[index])
            index += 1
            if not my_s[index-1].isdigit():
                inner(current.r) 
             
        inner(current)

    def calc(self):
        current = self.root
        def inner(current):
            if current == None:
                return 
            if (not current.v.lstrip("-").isdigit()) and \
                    current.l.v.lstrip("-").isdigit() and \
                    current.r.v.lstrip("-").isdigit():
                current.v = str(int(eval(f"{current.l.v}{current.v}{current.r.v}")))
                current.l = None
                current.r = None
            else:
                inner(current.l)
                inner(current.r)
        return inner(current)

    def __str__(self):
        current = self.root
        def inner(current):
            if not current.v.lstrip("-").isdigit():
                return f"({inner(current.l)}{current.v}{inner(current.r)})" 
            else:
                return current.v
        return inner(current)

def print_reduction(calculator):
    print("### print_reduction")
    print(calculator)
    while not str(calculator).lstrip("-").isdigit():
        calculator.calc()
        print(calculator)
