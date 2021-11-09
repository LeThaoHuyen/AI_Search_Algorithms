# ---------------- Greedy best-first search (Graph-search)---------------- #
import queue
from node import Node

def GBFS(graph, start, end, h):
    nNodes = len(graph)
    visited = [False]*nNodes
    explored = []
    path = [-1]*nNodes
    pq = queue.PriorityQueue()

    pq.put(Node(h[start], start))
    visited[start] = True
    
    while not pq.empty():
        node = pq.get()
        if node.id == end:
            return explored, path

        explored.append(node.id)

        for neighbor in graph[node.id]:
            if not visited[neighbor]:
                pq.put(Node(h[neighbor], neighbor))
                visited[neighbor] = True
                path[neighbor] = node.id

    return explored, -1



