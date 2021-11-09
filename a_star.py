# ---------------- A* search (graph search) ---------------- #
import queue
from node import Node

def A_star(graph, start, end, h):
    nNodes = len(graph)
    visited = [False]*nNodes
    path = [-1]*nNodes
    g = [float('inf')]*nNodes # store distance from start node to other nodes
    explored = []
    pq = queue.PriorityQueue()

    g[start] = 0
    pq.put(Node(0+h[start], start))

    while not pq.empty():
        node = pq.get()
        if node.id == end:
            return explored, path
        
        explored.append(node.id)
        visited[node.id] = True

        for neighbor in graph[node.id]:
            if not visited[neighbor] and g[node.id] + 1 < g[neighbor]:
                g[neighbor] = g[node.id] + 1
                f = g[neighbor] + h[neighbor]
                pq.put(Node(f, neighbor))
                path[neighbor] = node.id
    return explored, -1
