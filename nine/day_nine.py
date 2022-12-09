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

def two(): 
    ##WIP
    with open("nine/day_nine_test_two.txt", "r", encoding='utf-8') as f:
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
                            rope[i][0], rope[i][1] = last_pos[i-1]

                    if DIR == "L":
                        last_pos[i] = rope[i][::]
                        if i == 0: 
                            rope[i][0] -= 1
                            continue
                        last_relation = adjacent(last_pos[i], last_pos[i-1])
                        if (last_relation < 3) and (adjacent(rope[i], rope[i-1]) == 3):
                            rope[i][0], rope[i][1] = last_pos[i-1]

                    if DIR == "U":
                        last_pos[i] = rope[i][::]
                        if i == 0: 
                            rope[i][1] += 1
                            continue
                        last_relation = adjacent(last_pos[i], last_pos[i-1])
                        if (last_relation < 3) and (adjacent(rope[i], rope[i-1]) == 3):
                            rope[i][0], rope[i][1] = last_pos[i-1]

                    if DIR == "D":
                        last_pos[i] = rope[i][::]
                        if i == 0: 
                            rope[i][1] -= 1
                            continue
                        last_relation = adjacent(last_pos[i], last_pos[i-1])
                        if (last_relation < 3) and (adjacent(rope[i], rope[i-1]) == 3):
                            rope[i][0], rope[i][1] = last_pos[i-1]
                    
                visited.append((rope[-1][0], rope[-1][1]))
                debug_mask[rope[-1][1]][rope[-1][0]] = "X"

        ##pprint(debug_mask)
        print(len(set(visited)))

two()