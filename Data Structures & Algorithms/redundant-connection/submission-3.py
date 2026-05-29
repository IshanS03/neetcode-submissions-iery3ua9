class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        
        rank = [1] * (len(edges) + 1)
        par = [i for i in range(len(edges) + 1)]

        def find(x):
            
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):

            px, py = find(x), find(y)

            if px == py:
                return False
            
            if rank[px] > rank[py]:
                par[py] = px
                rank[px] += rank[py]
            else:
                par[px] = py
                rank[py] += rank[px]
            
            return True

        for edge in edges:

            if not union(edge[0], edge[1]):
                return edge
            
        
                

                
       
        


        