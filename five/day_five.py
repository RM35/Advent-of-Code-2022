## try everything until it works. 

def one():
    ans = ""
    crates = []
    with open("five/day_five_input.txt", "r") as f:
        stack = 0
        bot_stack = False
        while not bot_stack:
            for line in f.readlines():
                stack += 1
                if ord(line[1][0]) > 48 and ord(line[1][0]) < 58:
                    bot_stack = True
                    break
                else:
                    crates.append(line[1:-2:2])

    crates_two = [[] for x in range(len(crates[0]))]
    for i, crates_row in enumerate(crates):
        for j in range(len(crates[0])):
            if crates_row[j] == "": continue
            crates_two[j].append(crates_row[j])

    for i, c_row in enumerate(crates_two):
        crates_two[i] = list(filter(lambda x: x != " ", c_row))

    crates_two = crates_two[::2]

    with open("five/day_five_input.txt", "r") as f:
        orders = 0
        for line in f.readlines():
            line = line.rstrip()
            if line.startswith("move"):
                orders += 1
                amount = line.split(" ")[1]
                c_from = line.split(" ")[3]
                c_to = line.split(" ")[5]

                for i in range(int(amount)):
                    crates_two[int(c_to)-1].insert(0, crates_two[int(c_from)-1].pop(0))

    for i in crates_two:
        ans += str(i[0])

    assert(ans == "MQTPGLLDN")
      

def two():
    ans = ""
    crates = []
    with open("five/day_five_input.txt", "r") as f:
        stack = 0
        bot_stack = False
        while not bot_stack:
            for line in f.readlines():
                stack += 1
                if ord(line[1][0]) > 48 and ord(line[1][0]) < 58:
                    bot_stack = True
                    break
                else:
                    crates.append(line[1:-2:2])

    crates_two = [[] for x in range(len(crates[0]))]
    for i, crates_row in enumerate(crates):
        for j in range(len(crates[0])):
            if crates_row[j] == "": continue
            crates_two[j].append(crates_row[j])

    for i, c_row in enumerate(crates_two):
        crates_two[i] = list(filter(lambda x: x != " ", c_row))

    crates_two = crates_two[::2]

    with open("five/day_five_input.txt", "r") as f:
        orders = 0
        for line in f.readlines():
            line = line.rstrip()
            if line.startswith("move"):
                orders += 1
                amount = line.split(" ")[1]
                c_from = line.split(" ")[3]
                c_to = line.split(" ")[5]

                moved = []
                for i in range(int(amount)):
                    moved.append(crates_two[int(c_from)-1].pop(0))

                crates_two[int(c_to)-1] = moved + crates_two[int(c_to)-1]
    for i in crates_two:
        ans += str(i[0])

    assert(ans == "LVZPSTTCZ")

one()
two()