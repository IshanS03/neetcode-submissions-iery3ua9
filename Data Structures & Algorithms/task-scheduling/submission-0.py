class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        time = 0
        res = []
        presence = {}
        q = deque()

        presence = Counter(tasks)
        
        max_heap = [-val for val in presence.values()]
        heapq.heapify(max_heap)
           
        while max_heap or q:
            
            time +=1 

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt:
                    q.append([cnt, time + n])
            else:
                time = q[0][1]
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

            
        return time
