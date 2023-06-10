from truth_table_pretty_printer import *

if __name__ == "__main__":
    f0 = lambda x: 1-x
    f1 = lambda x,y: x&y
    f2 = lambda x,y: x|y
    f3 = lambda x,y,z: (x&y)|(x&z)
    f4 = lambda x1,x2,x3,x4,x5,x6,x7: f1(f0(x1),x2)| \
    (f2(x3,f0(x4))&x5)|f3(x5,x6,x7)
    pretty(f0, 1)
    pretty(f1, 2)
    pretty(f2, 2)
    pretty(f3, 3)
    pretty(f4, 7)
