# Probably some better recursive way of doing this.
# Didn't want to spend time googling so this is what
# I came up with. start at the "leafs" and sum the directory sizes.

lines = []
with open("seven/day_seven_input.txt", "r") as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))

objects = {}

current_directory = []
last_command = ""
log_lines = []
for line in lines:
    if line.startswith("$"):
        command = line.split(" ")[1]
        if command == "cd":
            last_command = "cd"
            if line.split(" ")[2] == "..":
                current_directory.pop()
            else:
                current_directory.append(line.split(" ")[2])
    
        if command == "ls":
            last_command = "ls"
        
    else:
        log_lines.append([current_directory[::], line])

for path, object in log_lines:
    path = "".join(i + "/" for i in path)
    if path not in objects:
        objects[path] = []
    if object.startswith("dir"):
        objects[path].append({"dir": object.split(" ")[1]})
    else:
        objects[path].append({"file": int(object.split(" ")[0])})

heir = []
for key, val in objects.items():
    heir.append([len(key.split("/")), key])

heir.sort()
heir = heir[::-1]

solved_sizes = {}

for i, key in heir:
    dir_total = 0
    for i, item in enumerate(objects[key]):
        if "dir" in item.keys():
            dir_total += solved_sizes[key+item["dir"]+"/"]
        if "file" in item.keys():
            dir_total += item["file"]
    
    solved_sizes[key] = dir_total

sum_of_smaller = 0
for path, size in solved_sizes.items():
    if size < 100000: sum_of_smaller += size

print(sum_of_smaller)

sizes_only = []
for path, size in solved_sizes.items():
    sizes_only.append(size)

TOTAL_SPACE = 70000000
NEEDED = 30000000

sizes_only.sort()

for i in range(len(sizes_only)):

    if sizes_only[-1] - sizes_only[i] < (TOTAL_SPACE - NEEDED):
        print(sizes_only[i])
        break
