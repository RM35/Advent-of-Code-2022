
def one():
    with open("two/day_two_input.txt", "r", encoding="utf-8") as f:
        count = 0
        cals = []
        for line in f.readlines():
            A = line.split(" ")[0]
            B = line.split(" ")[1].rstrip()
            if A == "A" and B == "X":
                count += 3
                count += 1
            if A == "B" and B == "Y":
                count += 3
                count += 2
            if A == "C" and B == "Z":
                count += 3
                count += 3
            if A == "A" and B == "Y":
                count += 6
                count += 2
            if A == "C" and B == "Y":
                count += 2
            if A == "B" and B == "Z":
                count += 6
                count += 3
            if A == "B" and B == "X":
                count += 1
            if A == "A" and B == "Z":
                count += 3
            if A == "C" and B == "X":
                count += 6
                count += 1
        print(count)

def two():
    with open("two/day_two_input.txt", "r", encoding="utf-8") as f:
        count = 0
        cals = []
        for line in f.readlines():
            A = line.split(" ")[0]
            B = line.split(" ")[1].rstrip()
            if B == "X": 
                count += 0
                if A == "A": count += 3
                if A == "B": count += 1
                if A == "C": count += 2
            if B == "Y": 
                count += 3
                if A == "A": count += 1
                if A == "B": count += 2
                if A == "C": count += 3
            if B == "Z": 
                count += 6
                if A == "A": count += 2
                if A == "B": count += 3
                if A == "C": count += 1
            pass
        print(count)
