class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        inDegree = [0] * numCourses

        for forLearn, toLearn in prerequisites:
            graph[toLearn].append(forLearn)
            inDegree[forLearn] += 1
        
        q = deque(i for i in range(numCourses) if inDegree[i] == 0)
        courseComp = 0

        while q:
            curCourse = q.popleft()
            courseComp += 1

            for nextCourse in graph[curCourse]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
        return numCourses == courseComp