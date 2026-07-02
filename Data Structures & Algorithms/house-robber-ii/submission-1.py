class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        first = nums[0:len(nums)-1]
        second = nums[1:]

        def dfs(i, nums):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            res = max(nums[i] + dfs(i+2, nums), dfs(i+1, nums))
            dp[i] = res
            return res

        dp = [-1] * (len(nums)-1)
        money1 = dfs(0, first)
        dp = [-1] * (len(nums)-1)
        money2 = dfs(0, second)
        return max(money1, money2)






