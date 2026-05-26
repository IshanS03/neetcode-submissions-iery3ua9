class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        path = set([])
        def dfs(course):

            if course in path:
                return False
            if preMap[course] == []:
                return True

            path.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
                
            path.remove(course)
            preMap[course] = []
            return True


        for course in range(numCourses):
            if(dfs(course)) == False:
                return False
        return True
