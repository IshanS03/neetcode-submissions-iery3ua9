class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > (n - 1):
            return False
            
        preMap = {i: [] for i in range(n)}

        for cur, nei in edges:
            preMap[cur].append(nei)
            preMap[nei].append(cur)

        visited = set()
        def dfs(node, par):

            if node in visited:
                return False


            visited.add(node)

            for nei in preMap[node]:

                if nei == par:
                    continue
                
                if not dfs(nei, node):
                    return False
                
            
            return True


        return dfs(0, -1) and len(visited) == n



        