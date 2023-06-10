from complex_number import *

if __name__ == "__main__":
    a = mycomplex(6,7)
    b = mycomplex(3.5,-8)
    c = a+b
    d = -9.5+c
    print("a :-", a)
    print("b :-", b)
    print("c = a+b :-", c)
    print("d = -9.5+c :-", d)
    e = a-b
    print("e = a-b :-", e)
    f = 7-b
    print("f = 7-b :-", f)
    g = e*f
    print("g = e*f :-", g)
    h = 7*g
    print("h = 7*g :-", h)
    i = mycomplex(0,-1)*mycomplex(0,-1)
    print("i :-", i)
    # j = a/g
    # print("j = a/g :-", j)
    # k = -1/a
    # print("k = -1/a :-", k)
    # z = a*(b+c)-d*(e+f-g)/(h+i*j)
    # print("z :-",z)