from math import *

def make_class(str):
    class aclass:
        def __repr__(self): return str 
    return aclass

empty = make_class ("empty")
full = make_class ("full")

class quadtree:
    def __init__(self, img):
        n=int(sqrt(len(img)))
        self.img = [img[n*offset:n*(offset+1)] for offset in range (0,n)]
        self.size=0
        self.inner_repr=self.build_quadtree (0,0, n, n) 
    
    def build_quadtree(self, x0, y0, x1, y1):
        tmp = sum([self.img[i][j] for i in range(x0,x1) for j in range(y0, y1)])
        if 0 < tmp < ((x1-x0)**2):
            xoffset = (x1-x0)//2
            yoffset = (y1-y0)//2
            return [self.build_quadtree(x0, y0, x0+xoffset, y0+yoffset), \
                    self.build_quadtree(x0, y0+yoffset, x0+xoffset, y1), \
                    self.build_quadtree(x0+xoffset, y0, x1, y0+yoffset), \
                    self.build_quadtree (x0+xoffset, y0+yoffset, x1, y1)]
        else:
            self.size +=1
        return empty() if tmp == 0 else full()
    
    def count (self):
        return (len(self.img[0])**2)-self.size