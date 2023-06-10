import re

def open_file(s):
    with open(s) as f:
        d = dict()
        for i in f.readlines():
            s_split = i.split(":")
            d[tuple(s_split[1].strip().replace(" ", "").split(","))] = s_split[0].strip()
    return d
synonyms = open_file("synonyms-list.txt")
# print(synonyms)

def replace_synonyms(s):
    tmp = []
    for word in re.split("([\W])", s):
        find = False
        for key in synonyms.keys():
            if word in key: 
                tmp.append(synonyms[key].upper())
                find = True
                break
        if not find:
            tmp.append(word)
    
    return "".join(tmp)
