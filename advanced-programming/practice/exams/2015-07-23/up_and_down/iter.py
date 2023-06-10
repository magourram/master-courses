class UpDownFile(object):
    def __init__(self, name): 
        self.l_file = []
        exclude = ['.', ',', ';', ':', '"', "'", '(', ')', '[', ']', '{', '}', ' ', '-', '\n']
        with open(name) as f:
            tmp = ""
            for i in f.read():
                if i not in exclude:
                    tmp += i
                elif tmp != '':
                    self.l_file += [tmp]
                    tmp = ""
        #print(self.l_file)
                

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1 
        if self.i >= len(self.l_file):
            raise StopIteration
        
        return self.l_file[self.i]
     
    def ungetw(self):
        if self.i < 0:
            raise StopIteration
        self.i -= 1
