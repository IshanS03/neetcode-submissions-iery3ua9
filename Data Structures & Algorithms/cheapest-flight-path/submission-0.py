class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        edges = collections.defaultdict(list)

        for u, v, w in flights:
            edges[u].append((v, w))

        minHeap = []

        for v, w in edges[src]:
            heapq.heappush(minHeap, (w, v, 1))

        while minHeap:

            w1, n1, s = heapq.heappop(minHeap)
                
            t = w1
            
            if n1 == dst:
                return t
            
            if s == k + 1:
                continue 

            for n2, w2 in edges[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2, s + 1))
            
        return -1

            



            