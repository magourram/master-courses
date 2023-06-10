res = sum(range(1,10))
L = 9
S = 3

def check_rows(s): return all([sum(i) == res for i in s])
def check_cols(s): return all([sum([j[i] for j in s]) == res for i in range(L)])
def tmp_grid(l): return all([sum(map(sum, l[i:i+S])) == res for i in range(0, len(l), S)])
def check_grid(s): return all([tmp_grid([s[j][i:i+S] for j in range (L)]) for i in range(0, L, S)])

def is_sudoku(s):
    return check_grid(s) and check_rows(s) and check_cols(s)