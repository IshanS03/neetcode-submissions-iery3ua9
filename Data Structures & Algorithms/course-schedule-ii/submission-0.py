class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        path = set()
        visit = set()
        output = []
        def dfs(course):
            
            if course in path:
                return False
            
            if course in visit:
                return True

            path.add(course)
            for pre in preMap[course]:

                if not dfs(pre):
                    return []
                
            path.remove(course)
            visit.add(course)
            output.append(course)
            return True
                
            
        for c in range(numCourses):
            
            if dfs(c) == False:
                return []
        
        return output
            