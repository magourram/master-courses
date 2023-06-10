from guarded_methods import *

class ToBeGuarded:
    @guarded(lambda x,y,z: (x**2+y**2)==z**2)
    def m1(self, x, y, z):
        print("### m1({0},{1},{2}) has been called!".format(x,y,z))
    @guarded(lambda x: x%2 == 0)
    def m2(self, i):
        print("### m2({0}) has been called!".format(i))
    @guarded(lambda x,y: x<y)
    def m3(self, x, y):
        print("### m3({0},{1}) has been called!".format(x,y))

if __name__ == "__main__":
    to_be = ToBeGuarded()
    to_be.m1(1,2,3)
    to_be.m1(3,4,5)
    # to_be.m2(5)
    # to_be.m3('a','b')
    # to_be.m2(7)
    to_be.m1(5,4,3)
    # to_be.m3(3.15, 3.156)
    # to_be.m2(3)
    # to_be.m3(25, 7)
