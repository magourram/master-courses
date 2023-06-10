from skin_an_object import *

if __name__ == "__main__":
    s = stack(5) # 5 is the stack dimension
    print(s)
    trend = True
    for i in range(-1,14):
        if s.is_empty():
            s.become({push}, {pop})
            trend = True
        elif s.is_full():
            s.become({pop}, {push})
            trend = False
        s.push(i) if trend else s.pop()
        print(s)
    print(s.__dict__)
    print(s.tmp(10))