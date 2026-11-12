from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)      # b unlocks a
            indeg[a] += 1

        result = []

        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        taken = 0
        while q:
            c = q.popleft()
            result.append(c)
            for nxt in graph[c]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        if len(result) != numCourses:
            return []
        return result