with open("output.txt", "w") as f:
    for row in grid:
        newrow = ""
        for char in row:
            newrow += char
        f.write(newrow + "\n")