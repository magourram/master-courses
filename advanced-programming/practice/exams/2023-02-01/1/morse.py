class Node(object):
    def __init__(self, left = None, right = None, parent = None, value_char = None, value_morse = None, final_value = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value_char = value_char   # a or b etc...
        self.value_morse = value_morse # . or _
        self.final_value = final_value # for example: if self.value_char is "b" the final value will be "_..."

class Trie(object):
    def build_trie(self):
        for i in range(len(self.l_morse)):
            tmp = self.root
            for ch in self.l_morse[i]:
                if ch == '.':
                    if tmp.left == None:
                        tmp.left = Node(value_morse = '.') 
                        tmp.parent = tmp
                    tmp = tmp.left
                if ch == '_':
                    if tmp.right == None:
                        tmp.right = Node(value_morse = '_') 
                        tmp.parent = tmp
                    tmp = tmp.right
            tmp.value_char = chr(ord('a') + i) 
            tmp.final_value = self.l_morse[i] 
            self.l[i] = tmp

    # def dfs(self):
    #     [print(i.value_char, i.final_value) for i in self.l]
    #     print()
    #     def wrapper(current):
    #         print(current.value_char, " ", current.final_value)
    #         if current.right != None:
    #             wrapper(current.right)
    #         if current.left != None:
    #             wrapper(current.left)
    #     return wrapper(self.root)
    
    def __init__(self, l_morse):
        self.root = Node()
        self.l_morse = l_morse
        self.l = [0] * len(l_morse) # It allow me to have the encode in O(1)
        self.build_trie()

class Morse(object):
    def __init__(self):
        l_morse = ['._', '_...', '_._.', '_..', \
                   '.', '.._.', '__.', '....', \
                   '..', '.___', '_._', '._..', \
                   '__', '_.', '___', '.__.', \
                   '__._', '._.', '...', '_', \
                   '.._', '..._', '.__', '_.._', \
                   '_.__', '__..']
        self.trie = Trie(l_morse)

    def decode(self, s):
        tmp = []
        current = self.trie.root
        for i in range(len(s)):
            if s[i] == ".":
                current = current.left 
            elif s[i] == "_":
                current = current.right 
            elif s[i] == "u":
                tmp.append(current.value_char)
                current = self.trie.root
            if s[i] == " " or i == len(s) - 1:
                tmp.append(current.value_char)
                tmp.append(" ")
                current = self.trie.root
        return ''.join(tmp)

    def encode(self, s):
        s = s.lower()
        tmp = []
        for i in range(len(s)):
            if s[i] == " " or i == len(s) - 1:
                tmp.append(" ")
            else:    
                tmp.append(self.trie.l[ord(s[i]) - ord('a')].final_value)
                if s[i + 1] != " ": 
                    tmp.append('u')
        return ''.join(tmp) 
