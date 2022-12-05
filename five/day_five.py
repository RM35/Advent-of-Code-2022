## Post solution summary:
# 1: list slice to get each row on the initial stacks.
# 2: check for ascii 48 to 58 to detect the end of the initial stacks
# 3: filter() to remove empty strings and take every other crate stack to
# tidy up unused data.
# 4: Find move commands by line starting "move". split and get the values
# 5: use pop/insert to move around the crates
# 6: for part 2 collect all the pops in each move and use + operator to
# basically do a list.extend() but to the front of each stack
# 7: crate stacks are in oreder top to bottom so take [0] for each top crate.

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