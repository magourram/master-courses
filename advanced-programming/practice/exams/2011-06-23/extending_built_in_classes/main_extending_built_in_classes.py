from extending_built_in_classes import *
import itertools

if __name__ == "__main__":
    ds = sorted_dict()
    d = {}
    x = itertools.count(0)
    for i in "zyxwvutsrqponmlkjihgfedcba":
        ds[i] = d[i] = next(x)
    print("sorted dict")
    for k,v in ds.items(): print(k,v)
    print("dict")
    for k,v in d.items(): print(k,v)
    print("sorted dict after removal")
    del ds['b']
    for k,v in ds.items(): print(k,v)
