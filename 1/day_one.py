## Post solution summary:
# 1: Sum each line. split groups of lines on newlines
# readlines already splits by newline "\n" so having another
# is the same as split("\n\n")

def one():
    with open("one/day_one_input.txt", "r") as f:
        count = 0
        cals = []
        for line in f.readlines():
            if line == "\n": 
                cals.append(count)
                count = 0
                continue
            count += int(line.rstrip())

        cals.sort()
        assert(cals[-1] == 71502) # Answer 71502

def two():
    with open("one/day_one_input.txt", "r") as f:
        count = 0
        cals = []
        for line in f.readlines():
            if line == "\n": 
                cals.append(count)
                count = 0
                continue
            count += int(line.rstrip())

        cals.sort()
        assert((cals[-1] + cals[-2] + cals[-3]) == 208191)

one()
two()