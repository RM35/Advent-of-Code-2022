- Need to find the best path given 30 "steps" (minutes) cost of traversal is 1 cost of releasing the value is 1. Value weight is valve pressure * steps remaining.
- Valves can be passed over and ignored to prevent spending 1 step. to reach better valves

- pt1: compute the best cost out of all the available nodes:
    - from the node currently on:
        - calculate the steps to any other node.
        - multiply its pressure value * remaining steps
        - Pick this node and travel to it and activate it.
        - repeat


![](testgraph.png)
![](testgraphtestpath.png)
