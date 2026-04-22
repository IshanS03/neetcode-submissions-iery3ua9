class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def dfs(i, cur, combo):

            if combo == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates):
                return 
            if combo + candidates[i] > target:
                return
            cur.append(candidates[i])
            dfs(i+1, cur, combo + candidates[i])

            cur.pop()
            
            new_i = i+1

            while new_i < len(candidates) and candidates[new_i] == candidates[i]:
                new_i += 1

            dfs(new_i, cur, combo)

        
        dfs(0, [], 0)
        return res