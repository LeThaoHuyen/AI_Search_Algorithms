# Node class to store node id and its priority
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