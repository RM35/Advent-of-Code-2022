from pprint import pprint

with open("ten/day_ten_input.txt") as f:
    data = f.readlines()
    cycle_count = 0
    check = [20, 60, 100, 140, 180, 220]
    register_values = [1]

    data2 = []
    for line in data:
        line = line.rstrip()
        if line.startswith("noop"):
            data2.append(["noop", 0])
        else:
            data2.append([line.split()[0], int(line.split()[1])])
        
    for i, line in enumerate(data2):
        if i < 1: continue
        if data2[i-1][0] == "addx":
            register_values.append(register_values[i-1] + data2[i-1][1])
        else:
            register_values.append(register_values[i-1])

cycle_counts = []
count = 0
for  line in data2:
    if line[0] == "noop": count += 1
    if line[0] == "addx": count += 2
    cycle_counts.append(count)

combined = list(zip(data2, register_values, cycle_counts))
combined.reverse()

signals = []
for i in check:
    for k, output in enumerate(combined):
        if output[2] < i:
            signals.append(combined[k-1][1] * i)
            break

print(sum(signals))


cycles_regs = []

def get_register_at_cycle(data, cycles):
    for k, output in enumerate(data):
        if output[2] < cycles:
            return combined[k-1][1]
        
for i in range(240):
    cycles_regs.append([i, get_register_at_cycle(combined, i)])

combined.reverse()

# brush these Nones under the carpet
for i in range(3):
    cycles_regs[i][1] = 1

cyc_count = 0
screen = []
for y in range(6):
    row = ""
    for x in range(40):
        xregister = cycles_regs[cyc_count][1]
        xsprite_coverage = [xregister, xregister+1, xregister+2]

        if x in xsprite_coverage:
            row += "#"
        else:
            row += "."
        cyc_count += 1

    screen.append(row)

for row in screen:
    print(row)