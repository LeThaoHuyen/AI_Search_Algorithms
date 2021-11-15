# Node class to store node id and its priority
class Node:
    def __init__(self, priority, id):
        self.priority = priority
        self.id = id
    def __lt__(self, other):
        # if 2 nodes have the same priority, choose the one comes first lexicographically
        if self.priority == other.priority:
            return str(self.id) <= str(other.id)
        else:
            return self.priority < other.priority