# Post solution changes. How awful can we make this look.

def one():
    with open("two/day_two_input.txt", "r", encoding="utf-8") as f:
        count = 0
        for line in f.readlines():
            # Convert the rock paper scissors to 1, 2, 3s from the byte values.
            A = ord(line.split(" ")[0]) % 64
            B = ord(line.split(" ")[1].rstrip()) % 87
            # Always add the 1, 2, 3 from the players choice to satisfy the rule
            count += B
            # Same value = draw. add 3.
            if A - B == 0: count += 3
            # i+1 in the 1, 2, 3 of answers always beats i.
            # reduce both numbers by 1 to start on 0 to work with mod. 
            # do nothing when we lose so only check for a win.
            if (B - 1) == (A % 3): count += 6
        assert(count == 13221) 


def two():
    with open("two/day_two_input.txt", "r", encoding="utf-8") as f:
        count = 0
        for line in f.readlines():
            # Convert the rock paper scissors to 1, 2, 3s from the byte values.
            A = ord(line.split(" ")[0]) % 64
            B = ord(line.split(" ")[1].rstrip()) % 87
            # Always add the 1, 2, 3 from the players choice to satisfy lose,
            # draw, win rule. similar to part one but * 3.
            count += (B - 1) * 3

            # For the second rule we can say that B indicates a direction to 
            # move along the list of possibilities as i+1 indicates a win i=i
            # a draw and i-1 = a loss.

            # We must draw if B == 2 therefore we must play what A plays so
            # add the score of what A is:
            if B == 2: 
                count += A
                continue

            # if we must win then add the value of the i+1 of A.
            # if we lose the add the calue of i-1
            if B == 3: 
                count += (A % 3) + 1
            else:
                count += ((A - 2) % 3) + 1
        assert(count == 13131) 
