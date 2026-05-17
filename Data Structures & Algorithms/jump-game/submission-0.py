class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        goal = len(nums)-1
        start = goal - 1
        while(goal != 0):
            
            if start < 0:
                return False

            if nums[start] + start >= goal:
                goal = start

            start -= 1

        return True