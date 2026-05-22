class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        sIntervals = sorted(intervals)
        res = [sIntervals[0]]
        count = 0
        for i in range(1, len(sIntervals)):

            if res[-1][1] <= sIntervals[i][0]:
                res.append(sIntervals[i])
            else:
                count += 1
                if res[-1][1] > sIntervals[i][1]:
                    res[-1] = sIntervals[i]

        return count

        