from math import lcm

data_t = {0: {"starting_items": [79, 98], "operation": lambda x: x * 19, "test": lambda x: x % 23 == 0, "true": 2, "false": 3, "inspect_count": 0},
          1: {"starting_items": [54, 65, 75, 74], "operation": lambda x: x + 6, "test": lambda x: x % 19 == 0, "true": 2, "false": 0, "inspect_count": 0},
          2: {"starting_items": [79, 60, 97], "operation": lambda x: x * x, "test": lambda x: x % 13 == 0, "true": 1, "false": 3, "inspect_count": 0},
          3: {"starting_items": [74], "operation": lambda x: x + 3, "test": lambda x: x % 17 == 0, "true": 0, "false": 1, "inspect_count": 0}}

data = {0: {"starting_items": [75, 75, 98, 97, 79, 97, 64], "operation": lambda x: x * 13, "test": lambda x: x % 19 == 0, "true": 2, "false": 7, "inspect_count": 0},
        1: {"starting_items": [50, 99, 80, 84, 65, 95], "operation": lambda x: x + 2, "test": lambda x: x % 3 == 0, "true": 4, "false": 5, "inspect_count": 0},
        2: {"starting_items": [96, 74, 68, 96, 56, 71, 75, 53], "operation": lambda x: x + 1, "test": lambda x: x % 11 == 0, "true": 7, "false": 3, "inspect_count": 0},
        3: {"starting_items": [83, 96, 86, 58, 92], "operation": lambda x: x + 8, "test": lambda x: x % 17 == 0, "true": 6, "false": 1, "inspect_count": 0},
        4: {"starting_items": [99], "operation": lambda x: x * x, "test": lambda x: x % 5 == 0, "true": 0, "false": 5, "inspect_count": 0},
        5: {"starting_items": [60, 54, 83], "operation": lambda x: x + 4, "test": lambda x: x % 2 == 0, "true": 2, "false": 0, "inspect_count": 0},
        6: {"starting_items": [77, 67], "operation": lambda x: x * 17, "test": lambda x: x % 13 == 0, "true": 4, "false": 1, "inspect_count": 0},
        7: {"starting_items": [95, 65, 58, 76], "operation": lambda x: x + 5, "test": lambda x: x % 7 == 0, "true": 3, "false": 6, "inspect_count": 0}}

data = data
rounds = 10000

# Need to maintain the divisibility of the numbers while reducing size so
# modulo by the lcm to loop the number in a reasonable range
lowest_common_multiple = lcm(19, 3, 11, 17, 5, 2, 13, 7)
lowest_common_multiple_test = lcm(23, 19, 13, 17)

for x in range(rounds):
    for monkey, mdata in data.items():
        mdata["starting_items"].reverse()
        while len(mdata["starting_items"]) > 0:
            item = mdata["starting_items"].pop()
            mdata["inspect_count"] += 1
            item = mdata["operation"](item)

            item = item % lowest_common_multiple
            ##item = item // 3

            if mdata["test"](item) is True:
                data[mdata["true"]]["starting_items"].append(item)
            else:
                data[mdata["false"]]["starting_items"].append(item)
        
inspections = [0 for _ in range(len(data))]

for monkey, mdata in data.items():
    inspections[monkey] = mdata["inspect_count"]

inspections.sort()

print((inspections[-1]) * inspections[-2])
pass