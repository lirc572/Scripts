def StrToHex(s):
    res = ''
    for i in s:
        res = hex(ord(i))[2:] + res
    return res

StrToDec = lambda s: int(StrToHex(s), 16)

