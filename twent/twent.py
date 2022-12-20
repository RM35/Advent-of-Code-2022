from copy import deepcopy

inp = list(map(int, open("twent/t").readlines()))

enc_len = len(inp)

states = []
for i, mix_val in enumerate(inp):
    states.append([i, mix_val])

for old_loc, mix_val in states:
    new_loc = None
    print(sorted(states))
    if mix_val == 0: continue
    if mix_val < 0: new_loc = (old_loc + mix_val) % enc_len
    if mix_val > 0: new_loc = (old_loc + mix_val) % enc_len
    for i in range(len(states)):
        if states[i] == [old_loc, mix_val]:
            states[i] = [new_loc, mix_val]
            continue
        if states[i][0] > old_loc and states[i][0] <= new_loc:
            states[i][0] -= 1


pass