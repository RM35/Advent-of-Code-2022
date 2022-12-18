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

- BFS coming out with 30k explored cells after setting the bounds to -2 to 30 for each axis. runs in seconds.

- Now to compare the p1 cells with explored cells and count faces adjacent