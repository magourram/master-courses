class Node():
    def __init__(self, v, s1=None, s2=None, s3=None, s4=None):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.v = v
        self.color = self.get_value()

    def get_value(self):
        cur = self.v[0][0] # 0, 1
        for i in range(len(self.v)):
            for j in range(len(self.v[i])):
                if self.v[i][j] != cur:
                    return ""
        return "empty" if cur == 0 else "full"

    @staticmethod
    def to_leaf(root):
        if root.color in ("empty", "full"):
            return root.color
        return [Node.to_leaf(root.s1), Node.to_leaf(root.s2), Node.to_leaf(root.s3), Node.to_leaf(root.s4)]

    def __str__(self):
        return self.color

class quadtree():
    def __init__(self, raw_img):
        self.raw_img = raw_img
        self.img = self.__img()
        self.size = 0
        self.root = Node(self.img)
        self.build_quadtree()
        self.inner_repr = Node.to_leaf(self.root)

    def get_qs(self, img):
        L = len(img[0])
        offset = int(L / 2)
        my_l = [[] for i in range(4)]

        for i in range(offset):
            for j in range(L):
                if j < offset:my_l[0].append(img[i][j])
                else:my_l[1].append(img[i][j])

        for i in range(offset, L):
            for j in range(L):
                if j < offset:my_l[2].append(img[i][j])
                else: my_l[3].append(img[i][j])
        return [Node(self.__create_matrix(i)) for i in my_l]

    def build_quadtree(self):
        root = self.root
        def inner(current):
            if current.color in ("empty", "full"):
                self.size += 1
                # print(current.color)
                return

            current.s1, current.s2, current.s3, current.s4 = self.get_qs(current.v)

            inner(current.s1)
            inner(current.s2)
            inner(current.s3)
            inner(current.s4)
        return inner(root)

    def __create_matrix(self, raw_img):
        L = len(raw_img)
        RL = int(L**0.5)
        return [raw_img[i:i+RL]for i in range(0,L,RL)]

    def __img(self):
        return self.__create_matrix(self.raw_img)

    def count(self):
        return (len(self.img[0])**2) - self.size
        