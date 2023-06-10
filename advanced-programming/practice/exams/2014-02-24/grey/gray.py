def memoization(F):
    def wrapper(*args):
        if not args in wrapper.cache:
            wrapper.cache[args] = F(*args)
        else:
            print("### cached value")
        return wrapper.cache[args] 
    wrapper.cache = dict()
    return wrapper

def inner(n):
    if n == 0:
        return [""]
    else:
        tmp = []
        for l in inner(n-1):
            tmp.append(str(0)+str(l))
        for l in reversed(inner(n-1)):
            tmp.append(str(1)+str(l))
        return tmp

def gray(n):
    for i in inner(n):
        yield i

def mgray(n):
    global inner
    inner = memoization(inner)
    return gray(n)

