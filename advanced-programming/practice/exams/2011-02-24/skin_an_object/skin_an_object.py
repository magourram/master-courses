import types

def push(self, n):
    if not self.is_full():
        self.data.append(n)
    else:
        raise Exception
    
def pop(self):
    if not self.is_empty():
        self.data.pop()
    else:
        raise Exception

class Skin(type):
    def become(self, ADD, REMOVE):
        ADD = list(ADD)
        REMOVE = list(REMOVE)
        self.__dict__[ADD[0].__name__] = types.MethodType(ADD[0], self)
        if self.__dict__.__contains__(REMOVE[0].__name__):
            del self.__dict__[REMOVE[0].__name__] 

    def __new__(cls, classname, supers, classdict):
        classdict["become"] = cls.become
        return type.__new__(cls, classname, supers, classdict)

class stack(object, metaclass = Skin):
    def __init__(self, dim):
        self.dim = dim
        self.data = []

    def is_empty(self):
        return self.data == []

    def is_full(self):
        return len(self.data) == self.dim -1

    def __str__(self):
        return f"Stack top :- {len(self.data)} Stack dim :- {self.dim} Stack data :- {self.data}"
    
