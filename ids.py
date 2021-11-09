# ---------------- Iterative deepening search ---------------- #

def IDS(graph, start, end):
    explored = [] # save explored nodes in order
    path = [start] # save path in order

    # depth-limit search
    def DLS(start, end, limit):
        '''
        Return types includes:
            + "failure": no solution
            + "cutoff": no solution within depth limit
            + path: have solution so return the path 
        '''
        if start == end: return path
        elif limit == 0: return "cutoff"

        cutoff = False

        explored.append(start)
        visited[start] = True

        graph[start].sort() #explored the smaller node first
        for node in graph[start]:
            # avoid loop by not visiting again the node on the current path
            if visited[node] == True: 
                continue
            # goal test is applied
            if node == end:
                path.append(end)
                return path # return solution

            path.append(node)
            result = DLS(node, end, limit-1) 

            if result == "cutoff": cutoff = True
            elif result != "failure": return path # return solution

            path.pop() # backtrack path

        visited[start] = False # backtrack

        if cutoff: return "cutoff"
        else: return "failure"

    limit = 1
    res = None
    while True:
        visited = [False]*len(graph)
        res = DLS(start, end, limit)
        if res == "failure":
            return explored, -1 # -1 means there is no path
        if res != "cutoff":
            return explored, path
        limit += 1





