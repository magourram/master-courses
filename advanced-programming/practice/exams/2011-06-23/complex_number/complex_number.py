class mycomplex():
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, x):
        if not isinstance(x, mycomplex):
            return mycomplex(x + self.r, self.i)
        else:
            return mycomplex(x.r + self.r, self.i + x.i)

    def __radd__(self, x):
        return self.__add__(x)

    def __sub__(self, x):
        if not isinstance(x, mycomplex):
            return mycomplex(x - self.r , - self.i)
        else:
            return mycomplex(self.r - x.r, self.i - x.i)
    
    def __rsub__(self, x):
        return self.__sub__(x)
    
    def __mul__(self, x):
        if not isinstance(x, mycomplex):
            return mycomplex(self.r * x, self.i * x)
        else:
            return mycomplex((self.r * x.r) - (self.i * x.i), \
                             (self.i * x.r) + (self.r * x.i))

    def __rmul__(self, x):
        return self.__mul__(x)
    
    def __str__(self):
        return f"{self.r}{self.i:+}i"
    