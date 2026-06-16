class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_p = nums[0]
        min_p = nums[0]
        size = len(nums)
        global_max = nums[0]

        for i in range(1, size):
            cur_max = max(nums[i], nums[i]*max_p, nums[i]*min_p)
            cur_min = min(nums[i], nums[i]*min_p, nums[i] * max_p)
            max_p = cur_max
            min_p = cur_min
            global_max = max(max_p, global_max)
            
        return global_max