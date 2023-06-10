import types
from pprint import pprint

class Switch(object):
    def match(z, n):
        my_dict = dict(self.__class__.__dict__.items())
        # pprint(my_dict)
        my_list = []
        for k,v in my_dict.items(): 
            if type(v) == types.FunctionType:
                if v.__name__ == "wrapper":
                    my_list.append(v(self, n))
        # pprint(my_list)
        my_list2 = []
        for i in my_list:
            if i != None:
                my_list2.append(i)
        return my_list2[0]  

def case(p):
    def decorator(F):
        def wrapper(self, args):
            # print("W", self, F, p, args)
            if type(p) == int:
                l = [p]
            elif "__iter__" in p.__class__.__dict__:
                l = list(p)
            if args in l or p == "default":
                return types.MethodType(F, self)
            return None
        return wrapper
    return decorator
