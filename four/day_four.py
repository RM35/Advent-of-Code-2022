def one():
    with open("four/day_four_input.txt", "r") as f:
        subset_count = 0
        for line in f.readlines():
            line = line.rstrip()
            
            r1 = list(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1))
            r2 = list(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))

            if set(r1).issubset(set(r2)):
                subset_count += 1
            elif set(r2).issubset(set(r1)):
                subset_count += 1

    assert(subset_count == 588)

def two():
    with open("four/day_four_input.txt", "r") as f:
        all_overlap = 0
        for line in f.readlines():
            line = line.rstrip()
            
            r1 = list(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1))
            r2 = list(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))

            if set(r1) & set(r2):
                all_overlap += 1

    assert(all_overlap == 911)

one()
two()
