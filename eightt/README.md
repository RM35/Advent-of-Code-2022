# Part 1:

Just implementation?

- Brute force each for adjacent should work on part 1
- potential for turning into a graph and running dijkstra to only check for cubes 1 distance away to save time

Brute force each with every other ran in ~10 seconds correct answer

# Part 2:

Finding the air pockets to subtract sounds like a BFS from the outside of the droplet.

- We then need to represent the 3D space as a graph. Let BFS run within a box bounded by the extremities of the droplet + 1.  Any piece of obsidian it reachs add that to the total faces.
- Cube is a total of 12K cells so ok

- Try without a grid? simplifiies not having to test boundaries and make sure there is boundaries. Just set the boundaries in the BFS.

- BFS coming out with 30k explored cells after setting the bounds to -2 to 30 for each axis. runs in 0.3 seconds in debug.

- Now to compare the p1 cells with explored cells and count faces adjacent. This is explored * droplets * 6 sides so 30K * 3K * 6 = 540K operations. Around a minute to run in debug. First answer 7646 is too large. Check test input.

- Fix: issue is the adjacency check is jsut returning true or false and the whole cell is keeping it's faces. The adjacency needs modified to return face reduction based on the number of adjacent explored.

- Can keep the adjacent function and just modify the counting loop. First attempt actually counted the faces not on the outside. Count the total surface and subtract this should be same. test is working.

- Correct p2 answer after another 1min runtime :)