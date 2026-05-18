class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = 0
        maxSum = -1000
        for num in nums:
            
            if (curSum < 0):
                curSum = num 
            else:
                curSum += num
            
            maxSum = max(curSum, maxSum)

        
        return maxSum
        
        
