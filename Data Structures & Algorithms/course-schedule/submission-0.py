class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #intution: calculate every courses indegree and if the total number of processed courses in this process is all the courses then its possible!
        taken = 0
        indegree = [0] * numCourses
        directed_graph = [[] for i in range(numCourses)]

        for prereq in prerequisites:
            directed_graph[prereq[1]].append(prereq[0]) 
            indegree[prereq[0]] += 1

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)


        while queue:
            curr_class = queue.pop()
            taken += 1

            for child in directed_graph[curr_class]:
                indegree[child] -= 1
                if indegree[child] == 0:                
                    queue.append(child)
        
        return True if taken == numCourses else False