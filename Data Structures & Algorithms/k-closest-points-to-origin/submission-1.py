class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        max_heap = []
        for point in points:
            distance = math.sqrt((point[0]*point[0]) + (point[1]*point[1]))
            heapq.heappush(max_heap, (-distance, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        closest_points = [item[1] for item in max_heap]
        return closest_points



        