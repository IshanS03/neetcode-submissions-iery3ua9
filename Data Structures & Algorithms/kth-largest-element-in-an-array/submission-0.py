class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        for i in range(k):
            res = -heapq.heappop(max_heap)
        
        return res