from collections import defaultdict

class BF_graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def traverse(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
g = BF_graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("BFS traversal starting from vertex 2:")
g.traverse(2)