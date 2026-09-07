class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # 1. Standard Kahn's Init: Graph & In-Degrees
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        # Track prerequisites for every single node using an array of sets
        prereqs_of = [set() for _ in range(numCourses)]
        
        # 2. Build connections (u -> v means u must be learned before v)
        for u, v in prerequisites:
            graph[u].append(v)
            in_degree[v] += 1
            prereqs_of[v].add(u) # u is a direct prerequisite of v
            
        # 3. Enqueue starting points (nodes with 0 prerequisites)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # 4. Process level-by-level BFS
        while queue:
            current_course = queue.popleft()
            
            for next_course in graph[current_course]:
                # THE KEY STEP: next_course inherits all dependencies from current_course
                prereqs_of[next_course].update(prereqs_of[current_course])
                
                # Standard Kahn's decrement
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
                    
        # 5. Evaluate queries instantly using our sets
        res = []
        for u, v in queries:
            res.append(u in prereqs_of[v])
            
        return res
