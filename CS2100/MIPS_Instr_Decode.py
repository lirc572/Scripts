decode = lambda code: [(lambda a: '0'*(4-len(a))+a)(bin(int(x, 16))[2:]) for x in code]
