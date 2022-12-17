# P1

Roughed out implementation didnt give the correct anser on test but did on input. Very untidy but that's just how it be.

I let it auto space and add to the grid but threw that out for a 4000 tall which would fit everything.

# P2

Should repeat the pattern eventually. 10091 right/left moves and 5 shapes. 50k to repeat given a flat floor every 50k.

there are many floor/stack variations permutations in 100s millions. This requires dynamic programming again, probably.


# 100MM stacks to see what the ratio of height to stacks does:
Ratio jumped around within the same rought 1000 or so during this check. Can't check
them all as we can't just verify a height given the rules? maybe. not sure.
![](Untitled2.png)



# 3 Find the pattern

There must be a repeating pattern. Maybe not as large as every 100m. if a repeating pattern is there then a subset of that patttern must also repeat. Therefore search for a repeating pattern of arbitrary size (say 20 rows) and find how often that repeats. Then expand it to find the start and end of the repeating pattern so that we can count how many rocks are in it and when it starts globally.