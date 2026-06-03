class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        
        q = deque()
        patterns = {}
        visited = set()
        
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                new_pattern = word[:i] + '*' + word[i+1:]
                if new_pattern not in patterns:
                    patterns[new_pattern] = []
                patterns[new_pattern].append(word)

    

        def bfs():
            
            layers = 1
            q.append(beginWord)
            while q:
                for _ in range(len(q)):
                    new_word = q.popleft()
                    if new_word == endWord:
                        return layers
                    visited.add(new_word)

                    for i in range(len(new_word)):
                        new_pattern = new_word[:i] + '*' + new_word[i+1:]
                        if new_pattern in patterns:
                            for word in patterns[new_pattern]:
                                if new_word != word and word not in visited:
                                    q.append(word)

                layers += 1
            return 0 
        return bfs()
       