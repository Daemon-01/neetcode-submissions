class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        inDegree = [0] * numCourses

        for forLearn, toLearn in prerequisites:
            graph[toLearn].append(forLearn)
            inDegree[forLearn] += 1
        
        q = deque(i for i in range(numCourses) if inDegree[i] == 0)
        courseComp = 0

        res = []

        while q:
            curCourse = q.popleft()
            res.append(curCourse)
            courseComp += 1

            for nextCourse in graph[curCourse]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
        return res if courseComp == numCourses else []