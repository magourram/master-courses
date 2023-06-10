def open_file(f="wordlist-7.txt"):
    res = []
    with open(f) as file:
        res = file.read().splitlines()
    return res

global l
l = open_file()

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []

def root_to_leaf(root, t, path, pathLength): 
    print(root, t, path, pathLength)

    if root is None:
        return

    if(len(path) > pathLength):
        path[pathLength] = root.value
    else:
        path.append(root.value)

    pathLength += 1

    if root.value == t:
        print(path[:pathLength])

    for i in root.children:
        root_to_leaf(i, t, path, pathLength) 
        

def dfs(root, c=0): 
    print(c, "\t" * c, root.value)

    for i in root.children:
        c += 1
        dfs(i, c)
        c -= 1 

def chain(f, t):
    root = Node(f)
    res = []

    def inner(current, f, t, visited=[]): 
        if current.value == t:
            # print(visited)
            # res.append(visited)
            return

        mask = [f[i] if f[i] == t[i] else " " for i in range(len(f))]
        for word in l:
            for i in range(len(word)):
                if mask[i] == " " and word[:i] + word[i+1:] == f[:i] + f[i+1:]:
                    if word not in visited:
                        current.children.append(Node(word))
                        break
          
        for ch in current.children:
            inner(ch, ch.value, t, visited+[ch.value])

    visited = []
    visited.append(f)
    inner(root, f, t, visited)
    root_to_leaf(root, t, [], 0)
    # dfs(root)
    return res
