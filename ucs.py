'''
Input format:
- N - size of maze
- Node 0's adjacency list
- Node 1's ..............
...
- Node (N*N-1)'s adjacency list
- E - exit node

Output format:
- The time to escape the maze
- The list of explored nodes
- The list of nodes on the path
'''
import queue

class Node:
    def __init__(self, priority, id):
        self.priority = priority
        self.id = id
    def __lt__(self, other):
        # if 2 nodes have the same priority, choose the one with smaller id
        if self.priority == other.priority:
            return self.id <= other.id
        else:
            return self.priority < other.priority

# ------------------ Uniform-cost search  ------------------
def UCS(graph, nNode, start, end):
    pq = queue.PriorityQueue() # frontier which is a priority queue
    explored = [] # array to save explored nodes in order
    visited = set() # a set to save explored node 
    path = [-1]*nNode # array to save pre node of a node on the path

    pq.put(Node(0,start))

    while not pq.empty():
        # pop the lowest-cost from frontier
        node = pq.get()

        # if this node is visisted we continue (*)
        # this condition acts like the step of removing the same node 
        # with higher path-cost in the frontier (the lowest one has been visited before)
        if node.id in visited:
            continue

        # if this node is the exit node return solution
        if node.id == end:
            return explored, path

        # add to explored set
        explored.append(node.id)
        visited.add(node.id)

        for neighbor in graph[node.id]:
            # considered node must be not expanded 
            # even if it has higher path cost than one in frontier we still put it in frontier 
            # cuz the priority queue and condition (*) above will guarantee not expanding it 
            if neighbor not in visited:
                pq.put(Node(node.priority + 1, neighbor))
                path[neighbor] = node.id

    return explored, -1 # -1 means there is no path

def printPath(path, start, end):
    if start == end:
        print(end, end = " ")
    else:
        if path[end] == -1:
            print("No path")
        else:
            printPath(path, start, path[end])
            print(end, end = " ")

n = int(input())
graph = [0]*(n*n)
for i in range(n*n):
    graph[i] = list(map(int, input().split()))
exitNode = int(input())

explored, path = UCS(graph, n*n, 0, exitNode)
print(len(explored))
print(*explored)
if path == -1: print("No path") 
else: printPath(path, 0, exitNode)



