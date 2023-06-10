#!/usr/bin/env python3

from pprint import pprint
import itertools

def get_primes(n):
    out = list()
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**.5 ) + 1)):
            out.append(num)
    return out

def goldbach(n):
    if n%2 == 0 and n > 2:
        list_primes = get_primes(n)
        l = list(filter(lambda x: sum(x) == n, list(itertools.combinations_with_replacement(list_primes, r=2))))
        return l

def goldbach_list(n, m):
    return dict(filter(lambda x: x[1] != None, {i:goldbach(i) for i in range(n, m)}.items()))
    

pprint(goldbach(18))
pprint(goldbach(16))
pprint(goldbach_list(1, 25))
