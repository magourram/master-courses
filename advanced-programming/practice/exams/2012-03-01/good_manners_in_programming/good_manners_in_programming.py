def private(*p_args):
    def decorator(CLS):
        class wrapper:
            def __init__(self, *args):
                self.wrapped = CLS(*args)
                self.p_args = p_args
            def __getattr__(self, attr):
                if attr in p_args: raise TypeError("private attribute fetch: " + attr)
                else: return getattr(self.wrapped, attr)
            def __setattr__(self, attr, val):
                if attr == "wrapped": self.__dict__[attr] = val
                elif attr in p_args: raise TypeError("private attribute change: " + attr)
                else: setattr(self.wrapped, attr, val)
        return wrapper
    return decorator

def add_method(wrapped, ttype, attr):
    def onGet(): return wrapped.__dict__[attr]
    def onSet(val): wrapped.__dict__[attr] = val
    name = ttype + attr[0].upper() + attr[1:]
    if ttype == "get": setattr(wrapped, name, onGet) # wrapped.__dict__[name] = onGet
    if ttype == "set": setattr(wrapped, name, onSet) # wrapped.__dict__[name] = onSet

def selectors(*s_args):
    def decorator(CLS):
        class wrapper:
            def __init__(self, *args):
                self.wrapped = CLS(*args)
                print(self.wrapped)
                for ttype, attrs  in s_args[0].items():
                    for attr in attrs:
                        if attr in self.wrapped.p_args: add_method(self.wrapped.wrapped, ttype, attr)
                        else: raise TypeError("attempt to add a selector for a non private attribute: " + attr)
            def __getattr__(self, attr):
                return getattr(self.wrapped, attr)
            def __setattr__(self, attr, val):
                if attr == "wrapped": self.__dict__[attr] = val
                else: setattr(self.wrapped, attr, val)
        return wrapper
    return decorator
