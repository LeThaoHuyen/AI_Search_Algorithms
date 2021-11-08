# AI_Search_Algorithms
This repository includes the implementations of 4 classic AI search algorithms:
- Uniform-cost search (UCS)
- Iterative deepening search that uses depth-first tree search as core component and avoids
loops by checking a new node against the current path
- Graph-search Greedy best-first search using the Manhattan distance as heuristic
- Graph-search A* using the same heuristic as above

## Input format for graph
The graph in this problem presents a maze of size NxN:

And it is inputted in the following format:
- The first line containes N
- The next NxN lines, each contains an adjacency list of node i
- The last line contains the exiting node

The example input for the maze given above is provided in input.txt file.

*Note: since the graph presents a maze, the weight of each edge equals 1. 

