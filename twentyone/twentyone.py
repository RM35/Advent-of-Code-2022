from collections import defaultdict

data = open("twentyone/i").readlines()

done_monkeys = set()
m_dict = defaultdict(str)
for line in data:
    line = line.strip()
    if len(line.split()) > 2:
        m_dict[line.split()[0][:-1]] = line.split()[1:4]
    else:
        m_dict[line.split()[0][:-1]] = line.split()[1]
        done_monkeys.add(line.split()[0][:-1])

while len(done_monkeys) < len(m_dict):
    for monkey, mdata in m_dict.items():
        if monkey in done_monkeys:
            continue
        if mdata[0] in done_monkeys and mdata[2] in done_monkeys:
            m_dict[monkey] = eval(f'{m_dict[mdata[0]]} {mdata[1]} {m_dict[mdata[2]]}')
            done_monkeys.add(monkey)

print(m_dict["root"])