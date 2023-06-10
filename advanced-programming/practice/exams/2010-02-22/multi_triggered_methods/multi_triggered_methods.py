def multi_triggered(*dec_args):
    mt_times = dec_args[0]
    mt_function = dec_args[1]
    def decorator(F):
        def wrapper(*args):
            if wrapper.count >= 2:
                wrapper.dict[F] = [mt_function(wrapper.dict[F][i], args[i+1]) for i in range(len(wrapper.dict[F]))]
            else:
                wrapper.dict[F] = [i for i in args[1:]]
            if wrapper.count == mt_times:
                wrapper.count = 1
                return F(args[0], *wrapper.dict[F])
            wrapper.count += 1
        wrapper.count = 1
        wrapper.dict = {}
        return wrapper
    return decorator

class ToBeMultiTriggered:
    def m1(self): print("### m1 has been called!")

    @multi_triggered(2, lambda x,y: x*y)
    def m2(self, i): print("### m2({0}) has been called!".format(i))

    @multi_triggered(3, lambda x,y: x+y)
    def m3(self, x, y): print("### m3({0},{1}) has been called!".format(x,y))

if __name__ == "__main__":
    to_be = ToBeMultiTriggered()
    to_be.m1()
    to_be.m2(5)
    to_be.m3('a',3)
    to_be.m2(7)
    to_be.m3('b', 5)
    to_be.m2(3)
    to_be.m3('c', 7)

'''
### m1 has been called!
### m2(35) has been called!
### m3(abc,15) has been called!
'''