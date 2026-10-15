from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #intuition: create adjacency graph, bfs and if checked node in visited false. Since its undirected, make sure to not go both ways exploration so keep track of where the current node came from

        adjacency = [[] for i in range(n)]
        for edge in edges:
            adjacency[edge[0]].append(edge[1])
            adjacency[edge[1]].append(edge[0])

        visited = set()
        queue = [(0, -1)]
        visited.add(0)
        while queue:
            node, parent = queue.pop()
            for neighbor in adjacency[node]:
                if parent == neighbor:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                queue.append((neighbor, node))

        print(len(visited))
        return len(visited) == n