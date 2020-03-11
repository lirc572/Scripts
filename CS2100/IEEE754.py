#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def DecimalToBinary(decimal = ""):
    res = ""
    if decimal[0] == '-':
        decimal = decimal[1:]
        res += '-'
    integer, fraction = decimal = decimal.split('.')
    integer_bin = bin(int(integer))[2:]
    fraction_bin = ""
    fraction = float("0." + fraction)
    while fraction != 0:
        fraction *= 2
        if fraction >= 1:
            fraction_bin += '1'
            fraction -= 1
        else:
            fraction_bin += '0'
    res += integer_bin + '.' + fraction_bin
    return res

def ConvertToIEEE754(decimal = ""):
    res = ""
    if decimal[0] == '-':
        decimal = decimal[1:]
        res += '1'
    else:
        res += '0'
    full_bin = DecimalToBinary(decimal)
    first_one, dp = 0, 0
    for i, v in enumerate(full_bin):
        if v == '1':
            first_one = i+1
            break
    for i, v in enumerate(full_bin):
        if v == '.':
            dp = i
    exponent = dp - first_one
    exponent = exponent if (exponent > -1) else (exponent + 1)
    exponent = bin(127 + exponent)[2:]
    exponent = '0' * (8-len(exponent)) + exponent
    res += exponent
    mantissa = full_bin.replace('.', '')
    while mantissa[0] == '0':
        mantissa = mantissa[1:]
    mantissa = mantissa[1:] + '0' * (24 - len(mantissa))
    res += mantissa
    return res

def parse_bin(s):
    t = s.split('.')
    return int(t[0], 2) + int(t[1], 2) / 2.**len(t[1])

def ConvertToDecimal(fp = ""):
    res = "" if fp[0] == '0' else "-"
    mantissa = '1.' + fp[-23:]
    mantissa = parse_bin(mantissa)
    print(mantissa)
    exponent = int(fp[1:1+8], 2)-127
    res += str(mantissa * (2 ** exponent))
    return res

if __name__ == "__main__":
    print("[1]Convert decimal number to IEEE754 format\n[2]Convert IEEE754 format to dedimal format")
    if (input() not in ('2', '[2]')):
        print("Number in decimal:\ne.g. -5.84375")
        decimal = input()
        f = ConvertToIEEE754(decimal)
        print("Single precision float in binary: ", f)
        print("In hexadecimal: ", hex(int(f, 2)))
    else:
        print("Number in IEEE754:\ne.g. 0xc0bb0000\n     0b11000000101110110000000000000000")
        fp = input()
        fp = str(bin(eval(fp)))[2:]
        f = ConvertToDecimal(fp)
        print("Decimal representation:", f)