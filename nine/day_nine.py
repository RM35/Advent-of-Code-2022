from pprint import pprint


def adjacent(H, T):
    if ((H[0] == T[0] + 1) and (H[1] == T[1])) or ((H[0] == T[0] - 1) and (H[1] == T[1])) or ((H[1] == T[1] - 1) and (H[0] == T[0])) or ((H[1] == T[1] + 1) and (H[0] == T[0])):
        return 0
    if ((H[0] == T[0] + 1) and (H[1] == T[1] + 1)) or ((H[0] == T[0] - 1) and (H[1] == T[1] + 1)) or ((H[0] == T[0] + 1) and (H[1] == T[1] - 1)) or ((H[0] == T[0] - 1) and (H[1] == T[1] - 1)):
        return 1
    if H == T:
        return 2
    return 3

def one():
    with open("nine/day_nine_input.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
        last_H_pos = [0, 0]
        last_relation = 2
        visited = []
        H = [0, 0]
        T = [0, 0]

        debug_mask = [["." for y in range(5)] for x in range(5)]

        for line in lines:
            DIR = line.rstrip().split(" ")[0]
            AMOUNT = int(line.rstrip().split(" ")[1])

            for i in range(AMOUNT):

                if DIR == "R":
                    last_H_pos = H[::]
                    H[0] += 1
                    if (last_relation < 3) and (adjacent(H, T) == 3):
                        T[0], T[1] = last_H_pos
                    last_relation = adjacent(H, T)

                if DIR == "L":
                    last_H_pos = H[::]
                    H[0] -= 1
                    if (last_relation < 3) and (adjacent(H, T) == 3):
                        T[0], T[1] = last_H_pos
                    last_relation = adjacent(H, T)

                if DIR == "U":
                    last_H_pos = H[::]
                    H[1] += 1
                    if (last_relation < 3) and (adjacent(H, T) == 3):
                        T[0], T[1] = last_H_pos
                    last_relation = adjacent(H, T)

                if DIR == "D":
                    last_H_pos = H[::]
                    H[1] -= 1
                    if (last_relation < 3) and (adjacent(H, T) == 3):
                        T[0], T[1] = last_H_pos
                    last_relation = adjacent(H, T)
                
                visited.append((T[0], T[1]))
                #debug_mask[T[1]][T[0]] = "X"

        pprint(debug_mask)
        print(len(set(visited)))


def cheapest_cell(L, D):
    costs = {}
    costs[(0, 1)] = abs(L[0] - D[0]) + abs(L[1] + 1 - D[1])
    costs[(0, -1)] = abs(L[0] - D[0]) + abs(L[1] - 1 - D[1])
    costs[(-1, 0)] = abs(L[0] - 1 - D[0]) + abs(L[1] - D[1])
    costs[(1, 0)] = abs(L[0] + 1 - D[0]) + abs(L[1] - D[1])
    costs[(1, 1)] = abs(L[0] + 1 - D[0]) + abs(L[1] + 1 - D[1])
    costs[(-1, 1)] = abs(L[0] - 1 - D[0]) + abs(L[1] + 1 - D[1])
    costs[(-1, -1)] = abs(L[0] - 1 - D[0]) + abs(L[1] - 1 - D[1])
    costs[(1, -1)] = abs(L[0] + 1 - D[0]) + abs(L[1] - 1 - D[1])

    min_cost = (0, 1)
    for k, v in costs.items():
        if v < costs[min_cost]:
            min_cost = k

    return min_cost
 
def two(): 
    with open("nine/day_nine_input.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
        last_H_pos = [0, 0]
        last_relation = 2
        visited = []
        rope = [[0, 0] for i in range(10)]
        last_pos = [[0, 0] for i in range(10)]

        debug_mask = [["." for y in range(28)] for x in range(28)]

        for line in lines:
            DIR = line.rstrip().split(" ")[0]
            AMOUNT = int(line.rstrip().split(" ")[1])

            for i in range(AMOUNT):
                for i, pos in enumerate(rope):
                    if DIR == "R":
                        last_pos[i] = rope[i][::]
                        if i == 0: 
                            rope[i][0] += 1
                            continue
                        last_relation = adjacent(last_pos[i], last_pos[i-1])
                        if (last_relation < 3) and (adjacent(rope[i], rope[i-1]) == 3):
                            rope[i][0] = rope[i][0]+cheapest_cell(rope[i], rope[i-1])[0]
                            rope[i][1] = rope[i][1]+cheapest_cell(rope[i], rope[i-1])[1]

                    if DIR == "L":
                        last_pos[i] = rope[i][::]
                        if i == 0: 
                            rope[i][0] -= 1
                            continue
                        last_relation = adjacent(last_pos[i], last_pos[i-1])
                        if (last_relation < 3) and (adjacent(rope[i], rope[i-1]) == 3):
                            rope[i][0] = rope[i][0]+cheapest_cell(rope[i], rope[i-1])[0]
                            rope[i][1] = rope[i][1]+cheapest_cell(rope[i], rope[i-1])[1]

                    if DIR == "U":
                        last_pos[i] = rope[i][::]
                        if i == 0: 
                            rope[i][1] += 1
                            continue
                        last_relation = adjacent(last_pos[i], last_pos[i-1])
                        if (last_relation < 3) and (adjacent(rope[i], rope[i-1]) == 3):
                            rope[i][0] = rope[i][0]+cheapest_cell(rope[i], rope[i-1])[0]
                            rope[i][1] = rope[i][1]+cheapest_cell(rope[i], rope[i-1])[1]

                    if DIR == "D":
                        last_pos[i] = rope[i][::]
                        if i == 0: 
                            rope[i][1] -= 1
                            continue
                        last_relation = adjacent(last_pos[i], last_pos[i-1])
                        if (last_relation < 3) and (adjacent(rope[i], rope[i-1]) == 3):
                            rope[i][0] = rope[i][0]+cheapest_cell(rope[i], rope[i-1])[0]
                            rope[i][1] = rope[i][1]+cheapest_cell(rope[i], rope[i-1])[1]
                    
                visited.append((rope[-1][0], rope[-1][1]))

        ##pprint(debug_mask)
        print(len(set(visited)))

two()