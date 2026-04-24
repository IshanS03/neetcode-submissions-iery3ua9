class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        res = []

        def dfs(used, combo):


            if len(combo) == len(nums):
                res.append(combo.copy())
                return

            for num in (nums):
                if num in used:
                    continue
                used.add(num)
                combo.append(num)
                dfs(used, combo)
                used.discard(num)
                combo.pop()

            
             
            
        dfs(set(), [])
        return res
            