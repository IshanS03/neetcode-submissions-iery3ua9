class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)

        
        visited = set()

        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:

                cur = q.popleft()
                for nei in adj[cur]:
                    
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        res = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1
        return res








        

        