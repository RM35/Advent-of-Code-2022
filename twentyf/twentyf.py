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
    while True:
        remainder = num % 5
        current = (remainder + carry)
        carry = 0
        if current == 3:
            carry = 1
            current = "="
        if current == 4:
            carry = 1
            current = "-"
        out += str(current)
        num = num//5
        if num == 0:
            if carry == 1:
                out += "1"
            break
    return out[::-1]

decimals = []
for num in data:
    decimal = convert(num)
    decimals.append(decimal)

goal = sum(decimals)

aa = 14
a = convert_d_to_s(aa)
b = convert(a)
print(a, b)
print(aa == b)

print(goal)
print(convert_d_to_s(goal))

# test result 2=-1=0

def show_all_fourdigit():
    chars = "=-012"

    with open("twentyf/o", "w") as f:
        for i in itertools.product(chars, repeat=4):
            stringed = "".join(x for x in i)
            outstr = f"{stringed} = {convert(stringed)}"
            f.write(outstr + "\n")
