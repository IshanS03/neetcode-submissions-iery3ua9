class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        minHeap = [[0, 0]] # cost, point
        seen = set()
        res = 0
        while len(seen) < N:

            c, p = heapq.heappop(minHeap)
            if p in seen:
                continue
            res += c
            seen.add(p)

            for neiCost, nei in adj[p]:
                if nei not in seen:
                    heapq.heappush(minHeap, [neiCost, nei])

        return res


