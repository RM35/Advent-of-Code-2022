## Post solution summary:
# 1: Simple to parse. Split each line in half with a slice.
# 2: Using lists and python "in" to check for the duplicate.
# 3: Make use of the ascii values to get the 1-26 26-55 values for letters

def one():
    with open("three/day_three_input.txt", "r") as f:
        bag1 = []
        bag2 = []
        for line in f.readlines():
            line = line.rstrip()
            first = line[int(len(line)/2):]
            last = line[:int(len(line)/2)]
            for char in first:
                if char in last:
                    if ord(char) < 91:
                        bag1.append(ord(char)-38)
                    else:
                        bag2.append(ord(char)-96)
                    break
        assert(sum(bag1) + sum(bag2) == 8240)
    
def two():
    with open("three/day_three_input.txt", "r") as f:
        group_badges = []
        lines = list(f.readlines())

        for i in range(0, len(lines), 3):
            elf_one = lines[i].rstrip()
            elf_two = lines[i+1].rstrip()
            elf_three = lines[i+2].rstrip()

            for item in elf_one:
                if item in elf_two and item in elf_three:
                    if ord(item) < 91:
                        group_badges.append(ord(item)-65+27)
                    else:
                        group_badges.append(ord(item)-96)
                    break
        assert(sum(group_badges) == 2587)

one()
two()