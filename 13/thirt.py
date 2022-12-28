from collections import deque

def compare(l1, l2):
    # Can be int int, int list or list list

    # Deal with list int/ int list
    if type(l1) is int and type(l2) is list: l1 = [l1]
    if type(l2) is int and type(l1) is list: l2 = [l2]

    # deal with int int. l1 less than or equal is correct
    # Need to distinguish if equal/below or above
    if type(l1) is int and type(l2) is int:
        if l1 == l2: return 0
        if l1 < l2: return -1
        if l1 > l2: return 1
    
    # deal with empty lists
    if type(l1) is list and type(l2) is list:
        if len(l1) == 0 and len(l2) > 0: return -1
        if len(l1) > 0 and len(l2) == 0: return 1
        if len(l1) == 0 and len(l2) == 0: return 0
    
    # deal with list list
    if type(l1) is list and type(l2) is list:
        min_len = min(len(l1), len(l2))
        for i in range(min_len):
            res = compare(l1[i], l2[i])
            if res == 1: return 1
            if res == -1: return -1

        # check if all were equal and l1 was shorter. Then correct order
        if (l1[min_len-1] == l2[min_len-1]) and len(l1) < len(l2): return -1

        # check if equal but l2 was shorter. incorrect order
        if (l1[min_len-1] == l2[min_len-1]) and len(l1) > len(l2): return 1

        # if all equal and equal length then ccontinue
        if (l1[min_len-1] == l2[min_len-1]) and len(l1) == len(l2): return 0

with open("thirt/thirt_input.txt","r") as f:
    lines = f.readlines()
    lines = list(filter(lambda x: x != "\n", lines))

right_order = []
index = 0
for i in range(0, len(lines), 2):
    index += 1
    l1 = eval(lines[i].strip())
    l2 = eval(lines[i+1].strip())
    result = compare(l1, l2)
    if result == -1: right_order.append(index)

print(right_order)
print(sum(right_order))

all_signals = []
for i in range(0, len(lines), 2):
    all_signals.append(eval(lines[i].strip()))
    all_signals.append(eval(lines[i+1].strip()))

total_below_6 = 0
total_below_2 = 0
for sig in all_signals:
    if compare(sig, [[6]]) == -1: total_below_6 += 1
    if compare(sig, [[2]]) == -1: total_below_2 += 1

print(total_below_6 + 2, total_below_2 + 1)
print((total_below_6 + 2) * (total_below_2 + 1))
# Test outputs
# True
# True
# False
# True
# False
# True
# False
# False