from ucs import UCS
from ids import IDS
from gbfs import GBFS
from a_star import A_star

def manhattanDis(n, node1, node2):
    x1, y1 = node1//n, node1%n
    x2, y2 = node2//n, node2%n
    return abs(x1-x2) + abs(y1-y2)

def heuristic(n, exitNode):
    h = [0]*(n*n)
    for i in range(n*n):
        h[i] = manhattanDis(n, i, exitNode)
    return h

def printPath(path, start, end):
    if start == end:
        print(end, end = " ")
    else:
        if path[end] == -1:
            print("No path")
        else:
            printPath(path, start, path[end])
            print(end, end = " ")

if __name__ == "__main__":
    # read input
    n = int(input())
    graph = [0]*(n*n)
    for i in range(n*n):
        graph[i] = list(map(int, input().split()))
    exitNode = int(input())

    # calculate heuristic function 
    h = heuristic(n, exitNode)

    print("Uniform-cost search result:")
    explored, path = UCS(graph, 0, exitNode)
    print(len(explored))
    print(*explored)
    if path == -1: print("No path") 
    else: printPath(path, 0, exitNode)
    print()

    print("Iterative deepening search result:")
    explored, path = IDS(graph, 0, exitNode)
    print(len(explored))
    print(*explored)
    if path == -1: print("No path") 
    else: print(*path)

    print("Greedy Best-first search result:")
    explored, path = GBFS(graph, 0, exitNode, h)
    print(len(explored))
    print(*explored)
    if path == -1: print("No path") 
    else: printPath(path, 0, exitNode)
    print()

    print("A* search result:")
    explored, path = A_star(graph, 0, exitNode, h)
    print(len(explored))
    print(*explored)
    if path == -1: print("No path") 
    else: printPath(path, 0, exitNode)