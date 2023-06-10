int_to_binary = lambda x, n: str(bin(x+2**n))[3:]
def generate_binary_list(n):
    for i in range(2**n):
        yield list(map(int, int_to_binary(i, n)))

def pretty(F, i):
    G = generate_binary_list(i)
    for i in G:
        print(i, F(*i))
