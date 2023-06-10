from collections import *
from pprint import pprint as p

eu = [
"iceland",
"ireland",
"portugal",
"united kingdom",
"france",
"spain",
"andorra",
"netherlands",
"belgium",
"luxembourg",
"switzerland",
"italy",
"san marino",
"vatican city",
"malta",
"norway",
"denmark",
"germany",
"liechtestein",
"sweden",
"poland",
"czech republic",
"austria",
"slovenia",
"croatia",
"bosnia and herzegovina",
"montenegro",
"albania",
"greece",
"finland",
"estonia",
"latvia",
"lithuania",
"russia",
"belarus",
"ukraine",
"moldova",
"romania",
"serbia",
"bulgaria",
"macedonia"
]

def build_dict(eu):
    d = defaultdict(list)
    for i in eu:
        d[i[0]].append(i)
    return d

def path(nation):
    d = build_dict(eu)
    def inner(nation, visited=[], res=[[]]):
        childs = list(set(d[nation[-1]]) - set(visited))
        if len(childs) == 0: 
            res.append(visited)
        for ch in childs: 
            inner(ch, visited + [ch])
        return res
    return max(inner(nation, [nation]), key=len)