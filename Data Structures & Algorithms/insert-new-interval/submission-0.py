class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for i, itvl in enumerate(intervals):

            if newInterval[1] < itvl[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > itvl[1]:
                res.append(itvl)
            else:
                newInterval[0] = min(newInterval[0], itvl[0])
                newInterval[1] = max(newInterval[1], itvl[1])
            
        res.append(newInterval)
        return res
            