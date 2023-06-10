def magic(magic_class): 
    def my_class(decorated_cls): 
        class wrapper:
            def __init__(self, *args):
                self.wrapped = decorated_cls(*args)

            def __settatt(self):
                for k, v in self.wrapped.__dict__.items():
                        if k != "wrapped":
                            setattr(magic_class, k, v)

            def __getattr__(self, attr):
                self.__settatt()
                setattr(magic_class, attr, decorated_cls.__dict__[attr])
                return getattr(self.wrapped, attr)
            
            def __setattr__(self, attr, value):
                if attr == "wrapped":
                    self.__dict__[attr] = value
                tmp = setattr(self.wrapped, attr, value)
                self.__settatt()
                return tmp
            
        return wrapper
    return my_class
