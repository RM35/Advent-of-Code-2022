from collections import deque

def compare(l1, l2):
    equal = True
    if equal == False: return False

    if type(l1) is int and type(l2) is list: l1 = [l1]
    if type(l2) is int and type(l1) is list: l2 = [l2]

    print(f'Comparing {l1} and {l2}')

    if type(l1) is int and type(l2) is int:
        print(f'Comparison: {l1 <= l2}')
        return l1 <= l2

    if type(l1) is list and type(l2) is list:
        if len(l1) == 0 and len(l2) > 0:
            print(f'Comparison: True')
            return True
            
        if len(l1) > 0 and len(l2) == 0: 
            print(f'Comparison: False')
            equal = False
            return False

    if type(l1) is list and type(l2) is list:

        final_depth = True
        for signal in l1:
            if type(signal) is list: 
                final_depth = False
        for signal in l2:
            if type(signal) is list: 
                final_depth = False
        
        if final_depth:
            min_len = min(len(l1), len(l2))
            for i in range(min_len):
                print(f'Comparing {l1[i]} and {l2[i]}')
                if l1[i] > l2[i]: 
                    print(f'Comparison: False')
                    equal = False
                    return False
                if i == (min_len-1) and len(l1) > len(l2) and l1[i] == l2[i]:
                    print(f'Comparison: False')
                    equal = False
                    return False
                if i == (min_len-1) and len(l1) == len(l2) and l1[i] == l2[i]:
                    print(f'Comparison: True')
                    return True
                if l1[i] < l2[i]: return True
            
        else:
            for i in range(min(len(l1), len(l2))):
                if equal == False: continue
                equal = compare(l1[i], l2[i])

    return equal

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
    print(result)
    print("")
    print("")
    if result: right_order.append(index)

print(right_order)
print(sum(right_order))

# Test outputs
# True
# True
# False
# True
# False
# True
# False
# False
