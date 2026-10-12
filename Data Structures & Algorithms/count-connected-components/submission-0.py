class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0: return 0
        result = 0
        adjacency = [[] for i in range(n)]
        for edge in edges:
            adjacency[edge[0]].append(edge[1])
            adjacency[edge[1]].append(edge[0])

        visited = set()

        for i in range(n):
            if i in visited:
                continue
            result += 1
            stack = [i]
            while stack:
                curr = stack.pop()
                visited.add(curr)
                for neighbor in adjacency[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result