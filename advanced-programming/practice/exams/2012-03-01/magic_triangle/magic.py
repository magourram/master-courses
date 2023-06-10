def magic():
    layer = 5
    res = 5
    while True:
        yield res 
        layer += 5*2
        res += layer
        