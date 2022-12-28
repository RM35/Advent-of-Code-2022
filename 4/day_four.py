import re

## Post solution summary:
# 1:  Parse using regex to split on multi characters
# 2: part one and 2 both make use of sets to check for the subset and any over
# lap can be checking for a bitwise and between sets

def one():
    subset_count = 0
    with open("four/day_four_input.txt", "r") as f:
        for line in f.readlines():
            ranges = [int(x) for x in re.split(r"[,-]", line.rstrip())]
            r1 = set(range(ranges[0], ranges[1] + 1))
            r2 = set(range(ranges[2], ranges[3] + 1))
            
            if r1.issubset(r2):
                subset_count += 1
            elif r2.issubset(r1):
                subset_count += 1

    assert(subset_count == 588)

def two():
    all_overlap = 0
    with open("four/day_four_input.txt", "r") as f:
        for line in f.readlines():
            ranges = [int(x) for x in re.split(r"[,-]", line.rstrip())]
            r1 = set(range(ranges[0], ranges[1] + 1))
            r2 = set(range(ranges[2], ranges[3] + 1))

            if r1 & r2:
                all_overlap += 1

    assert(all_overlap == 911)

one()
two()
