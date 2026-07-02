class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1] * (amount+1)

        def dfs(amount):
            
            if amount == 0:
                return 0
            if dp[amount] != -1:
                return dp[amount]

            res = 1e9

            for i in range(len(coins)):
                if amount - coins[i] >= 0: 
                    res = min(res, 1 + dfs(amount - coins[i]))

            dp[amount] = res
            return res 
        
        minCoins = dfs(amount)
        if minCoins >= 1e9:
            return -1
        else:
            return minCoins