from math import perm
import itertools

data = open("twentyf/i").readlines()
data = list(map(lambda x: x.rstrip(), data))


def convert(num):
    num = list(num)[::-1]
    pow = 1
    out_num = 0
    for digit in num:
        if digit == "1" or digit == "2":
            out_num += int(digit) * pow
        if digit == "-":
            out_num -= pow*1
        if digit == "=":
            out_num -= pow*2
        pow *= 5
    return out_num

def convert_d_to_s(num):
    out = ""
    carry = 0
    while num > 0:
        remainder = num % 5
        current = (remainder + carry)
        if current == 3:
            carry = 1
            current = "-"
        if current == 4:
            carry = 1
            current = "="
        out += str(current)
        num = num//5
    return out

decimals = []
for num in data:
    decimal = convert(num)
    decimals.append(decimal)

goal = sum(decimals)

print(convert_baseten_to_basefive(goal+2))


def show_all_fourdigit():
    chars = "=-012"

    with open("twentyf/o", "w") as f:
        for i in itertools.product(chars, repeat=4):
            stringed = "".join(x for x in i)
            outstr = f"{stringed} = {convert(stringed)}"
            f.write(outstr + "\n")
