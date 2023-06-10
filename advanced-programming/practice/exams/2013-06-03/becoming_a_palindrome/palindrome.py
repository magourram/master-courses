def palin(s):
    res = []
    for i in range(1, len(s)+1): res.append(DNA(s, i)); res.append(DNA(s[::-1], i))
    for i in max(res, key=len): s = s.replace(i, "", 1) 
    return s

def DNA(s, i): return [s[-i:][x] for x in range(i) if s[-i:][x] == s[::-1][:i][x]]

# def palin(s):
#     res = []
#     for i in range(1, len(s)+1):
#         res.append(tmp(s, s[::-1], i))
#         res.append(tmp(s[::-1], s, i))
#     for i in max(res, key=len):
#         s = s.replace(i, "", 1) 
#     return s

# def tmp(s, r_s, i):
#     p1 = s[-i:]
#     p2 = r_s[:i]
#     c = list()
#     for x in range(i):
#         if p1[x] == p2[x]:
#             c.append(p1[x])
#     return c
