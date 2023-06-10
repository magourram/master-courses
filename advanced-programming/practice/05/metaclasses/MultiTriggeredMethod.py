def caching(cache, *args, funct):
    if cache == []: return list(args[1:])
    return [funct(cache[j], args[j+1]) for j in range(len(args)-1)]

def multi_triggered(n, cacher):
    def actual_decorator(f):
        def make_decorator(*args):
            make_decorator.count += 1
            make_decorator.stored = caching(make_decorator.stored, *args, funct=cacher)
            if make_decorator.count == n:
                make_decorator.count = 0
                return f(args[0], *make_decorator.stored)
        make_decorator.count = 0
        make_decorator.stored = []
        return make_decorator
    return actual_decorator

def MultiTriggered(rules):
    class Meta(type):
        def __new__(cls, classname, supers, classdict):
            for attr, attrfun in classdict.items():
                if attr in rules.keys():
                    classdict[attr] = multi_triggered(*(rules[attr]))(attrfun)
            return type.__new__(cls, classname, supers, classdict)
    return Meta

# class MT(metaclass=MultiTriggered(\
#            {'m2':[2, lambda x, y: x*y],\
#             'm3':[3, lambda x, y: x+y]}\
#     )):
class MT:
    def m1(self):
        print("m1 has been called!")
    def m2(self, i):
        print("m2({0}) has been called!".format(i))
    def m3(self, x, y):
        print("m3({0},{1}) has been called!".format(x, y))

MT = MultiTriggered({'m2':[2, lambda x, y: x*y],'m3':[3, lambda x, y: x+y]})('MT', (), dict(MT.__dict__))

if __name__ == "__main__":
    mt = MT()
    mt.m1()
    print('### after the 1ˢᵗ call to m1')
    mt.m2(5)
    print('### after the 1ˢᵗ call to m2')
    mt.m3('a', 3)
    print('### after the 1ˢᵗ call to m3')
    mt.m2(7)
    print('### after the 2ⁿᵈ call to m2')
    mt.m3('b', 5)
    print('### after the 2ⁿᵈ call to m3')
    mt.m2(3)
    print('### after the 3ʳᵈ call to m2')
    mt.m3('c', 7)
    print('### after the 3ʳᵈ call to m2')