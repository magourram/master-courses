# from quadtree import *
from prof import *

if __name__ == "__main__":
    img0 = [0]*2+[1,0]+[0]*3+[1]*3+[0]*2+[1]*4
    img1 = [1]*12+[0]*4+[1]*12+[0]*4+[1]*12+[0]*4+[1]*12+[0]*4+ \
    [1]*8+[0,0]+[1]*14+[0,0]+[1]*14+[0,0]+[1]*14+[0,0]+ \
    [1]*6+[0]*8+[1,1,0,0]+[1]*4+[0]*8+[1,1,0,0]+[1]*4+ \
    [0]*8+[1,1,0,0]+[1]*4+[0]*8+[1,1,0,0]+[1]*4+[0]*14+ \
    [1]*2+[0]*14+[1]*2+[0]*13+[1]+[0]*14+[1]+[0]*3
    print(img0)
    q0 = quadtree(img0)
    print(q0.img)
    print(q0.inner_repr)
    print("vector size :- {0} quadtree size :- {1} saved space :- {2}".format(len(img0), q0.size, q0.count()))
    print(img1)
    q1 = quadtree(img1)
    print(q1.img)
    print(q1.inner_repr)
    print("vector size :- {0} quadtree size :- {1} saved space :- {2}".
    format(len(img1), q1.size, q1.count())) 
