class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        subset = []
        res = []

        def dfs(i, curSum):
            
            if curSum == target:
                res.append(subset.copy())
                return

            if i>=len(nums):
                return

            if curSum > target:
                return
            
            subset.append(nums[i])
            curSum += nums[i]
            dfs(i, curSum)

            curSum -= nums[i]
            subset.pop()
            dfs(i+1, curSum)
        
        dfs(0, 0)
        return res
            
