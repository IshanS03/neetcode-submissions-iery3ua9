class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        s_intervals = sorted(intervals)
        s_queries = sorted(queries)

        minHeap = []
        output = []
        res = {}
        i = 0
        for q in s_queries:
            while i < len(s_intervals) and s_intervals[i][0] <= q:
                l, r = s_intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]

        
                







