class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = {}

        # min operations to turn word1[i:] into word2[j:]
        def backtrack(i, j):

            # base cases: one string is exhausted.
            if i == len(word1): 
                return len(word2) - j
            if j == len(word2): 
                return len(word1) - i

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                # free move — no cost, both pointers advance
                dp[(i, j)] = backtrack(i + 1, j + 1)
                return dp[(i, j)]

            replaced = backtrack(i + 1, j + 1)   # swap word1[i] 
            deleted  = backtrack(i+1, j)           # drop word1[i]
            inserted = backtrack(i, j+1)           # add word2[j] 
            dp[(i, j)] = 1 + min(replaced, deleted, inserted)
            return dp[(i, j)]

        return backtrack(0, 0)









        