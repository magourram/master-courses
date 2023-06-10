import itertools

def grid_permutations():
    loop_unroll = list(itertools.product(range(0,24), range(0,24), range(0,24), range(0,24)))
    Ps = list(itertools.permutations(range(1,5)))
    for i in range(0,len(loop_unroll)):
        S = [Ps[loop_unroll[i][j]] for j in range(0,4)]
        yield S
    raise StopIteration

def sudoku():
    p = grid_permutations()
    while True:
        s = next(p)
        if test_columns(s) and test_squares(s): yield s

def test_columns(s):
    for j in range(0,4):
        if len({s[i][j] for i in range(0,4)}) < 4:
            return False
    return True

def test_squares(s):
    for offx in [0,2]:
        for offy in [0,2]:
            if len({s[x+offx][y+offy] for x in range(0,2) for y in range(0,2)})< 4:
                return False
    return True
