from collections import defaultdict

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

directions = [(1,0), (0,1), (-1,0), (0,-1)] 
def sum_tuple(cur, next): return [cur[0] + next[0], cur[1] + next[1]]
def update(x, y): return ((x-1) % 6 == 0 and (y - 1) % 4 or ((x+1) % 6 == 0 and (y + 1) % 4))

def c():
    def inner(i): 
        c.start = sum_tuple(c.start, directions[c.cur])
        c.res[tuple(c.start)].append(i)
        if isPrime(i): c.cur = update(i, c.cur)

    c.start = [0,0]
    c.cur = 0
    c.res = defaultdict(list) 
    c.res[(0,0)].append(3)

    [inner(i) for i in range(5, 2000, 2)]
    return c.res

def crossing(): return list(filter(lambda x: len(x) >= 2, c().values()))
