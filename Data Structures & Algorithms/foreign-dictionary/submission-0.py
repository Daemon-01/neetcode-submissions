from collections import deque

class Solution:
    # 🔧 CHANGED THE NAME HERE TO MATCH THE PLATFORM GRADER
    def foreignDictionary(self, words: list[str]) -> str:
        # 1. Initialize the graph and in-degree maps for EVERY unique character
        adj = {char: set() for word in words for char in word}
        in_degree = {char: 0 for word in words for char in word}
        
        # 2. Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
                
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    break  
                    
        # 3. Add all characters with an in-degree of 0 to the BFS queue
        q = deque([char for char in in_degree if in_degree[char] == 0])
        
        # 4. Process level-by-level BFS to form the topological sort string
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                    
        # 5. Cycle/Validity Check
        return "".join(res) if len(res) == len(in_degree) else ""
