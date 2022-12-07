def one():
    with open("seven/day_seven_test.txt", "r") as f:
        for line in f.readlines():
            print("one")

def two():
    with open("seven/day_seven_test.txt", "r") as f:
        for line in f.readlines():
            print("two")

one()
two()