with open("day_one_input.txt", "r", encoding="utf-8") as f:
    count = 0
    cals = []
    for line in f.readlines():
        if line == "\n": 
            cals.append(count)
            count = 0
            continue
        count += int(line.rstrip())

    cals.sort()
    print(cals[-1])
    print(cals[-1] + cals[-2] + cals[-3])