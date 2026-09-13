class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neig = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neig[pattern].append(word)
        
        q , visit = deque([(beginWord, 1)]), set([beginWord])

        while q:
            curWord, steps = q.popleft()

            if curWord == endWord:
                return steps
            for j in range(len(curWord)):
                pattern = curWord[:j] + "*" + curWord[j+1:]
                for word in neig[pattern]:
                    if word not in visit:
                        q.append((word, steps+1))
                        visit.add(word)
                neig[pattern] = []
        return 0