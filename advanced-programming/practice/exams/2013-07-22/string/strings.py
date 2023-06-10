from collections import defaultdict
from pprint import pprint as p

def reverse(s): 
    return s if len(s) <= 1 else s[-1] + reverse(s[:-1])

def strip(s, chars):
    return s if len(s) <= 1 else (s[0] if s[0] not in chars else "") + strip(s[1:], chars)

def split(s, seps):
    l = []
    def inner(s, seps, current=""):
        if len(s) == 0: return
        if s[0] in seps and current != "":
            l.append(current)
            current = ""
        current += s[0] if s[0] not in seps else ""
        inner(s[1:], seps, current)
    inner(s, seps)
    return l

def __find(s, ch, i=0):
    if len(s) == 0:
        return -1
    if s[0] == ch:
        return i
    return __find(s[1:], ch, i+1)

def find(s, ch):
    if find.memo.__contains__(s) and find.memo[s].__contains__(ch):
        tmp_res = __find(s[find.memo[s][ch]+1:], ch)
        if tmp_res == -1:
            return -1
        tmp = find.memo[s][ch] + tmp_res + 1
    else:
        tmp = __find(s, ch)
    find.memo[s][ch] = tmp
    return tmp

find.memo = defaultdict(defaultdict)
