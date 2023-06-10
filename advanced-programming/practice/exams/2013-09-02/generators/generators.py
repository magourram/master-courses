def even(G):
    while True:
        el = next(G)
        if el % 2 == 0:
            yield el

def stopAt(G, n):
    el = next(G)
    while el <= n:
        yield el
        el = next(G)

def buffer(G, n): 
    tmp = []
    try:
        while True:
            if len(tmp) == n:
                yield tmp
                tmp = []
            tmp.append(next(G))
    except StopIteration as si:
        yield tmp
            
def conditional(G, f):
    first = next(G)
    second = next(G)

    while True:
        if f(second):
            yield first
        first = second
        second = next(G)
