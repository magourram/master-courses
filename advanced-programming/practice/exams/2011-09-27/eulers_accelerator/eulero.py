def fact(n):
    if n <= 1:
        return n
    return fact(n-1) * n

def pi_series():
    denominator = 1
    t = True
    res = 0
    while True:
        if t: 
            res = 4 / denominator
            t = False
        else:
            res = - (4 / denominator)
            t = True
        denominator += 2
        yield res

def e_series():
    denominator = 0
    res = 1
    while True:
        if denominator == 0:
            res = 1
        else:
            res += 1 / fact(denominator) 
        denominator += 1
        yield res

# It is not correct?!
def euler_accelerator(F):
    n_m1 = next(F)
    n = next(F)
    n_p1 = next(F)

    while True:
        yield n_p1 - (((n_p1-n)**2)/((n_m1-2)*(n+n_p1)))
        n_m1 = n
        n = n_p1
        n_p1= next(F)
