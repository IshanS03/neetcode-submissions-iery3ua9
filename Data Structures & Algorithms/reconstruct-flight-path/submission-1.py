class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj_list = defaultdict(list)

        for u, v in tickets:
            heapq.heappush(adj_list[u], v)

        if "JFK" not in adj_list:
            return None

        current_city = "JFK"
        res = []

        def dfs(current_city: str):
            
            while adj_list[current_city] != []:
                nxt = heapq.heappop(adj_list[current_city])
                dfs(nxt)
            res.append(current_city)


        dfs("JFK")
        res.reverse()
        return res

        
