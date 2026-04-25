class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        def dfs(i, subset):
            
            if (i >= len(nums)):
                res.append(subset.copy())
                return 

            new_i = i+1 

            while new_i < len(nums) and nums[i] == nums[new_i]:
                new_i +=1
            subset.append(nums[i])
            dfs(i+1, subset)

            subset.pop()
            dfs(new_i, subset)
            
        dfs(0, [])
        return res