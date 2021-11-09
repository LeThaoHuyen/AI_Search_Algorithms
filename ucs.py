# ------------------ Uniform-cost search  ------------------ #
import queue
from node import Node

def UCS(graph, start, end):
    nNodes = len(graph)
    explored = [] # array to save explored nodes in order
    visited = set() # a set to save explored node 
    path = [-1]*nNodes # array to save pre node of a node on the path
    pq = queue.PriorityQueue() # frontier which is a priority queue

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





