class sorted_dict(dict):
    def items(self):
        return [(i,self[i]) for i in sorted(list(self))]
