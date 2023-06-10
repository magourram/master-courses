from pprint import pprint as p
import types

class Switch(object):
    def match(*args):
        s_dict = dict(args[0].__class__.__dict__)
        # p(s_dict)
        default = None
        for _, v in s_dict.items():
            if type(v) == types.FunctionType and v.__name__ == "wrapper":
                if v.case_arg == "default":
                    default = types.MethodType(v, args[0])
                elif "__iter__" in v.case_arg.__class__.__dict__ and args[1] in v.case_arg:
                    return types.MethodType(v, args[0])
                elif args[1] == v.case_arg:
                    return types.MethodType(v, args[0])    
        return default

def case(case_arg):
    def decorator(F):
        def wrapper(*args):
            # print("self ", *args)
            return F(*args)
        wrapper.case_arg = case_arg
        return wrapper
    return decorator
