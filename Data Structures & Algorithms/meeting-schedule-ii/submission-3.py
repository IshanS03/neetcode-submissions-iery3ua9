"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        sIntervals = sorted(intervals, key=lambda x: x.start)
        ends = []
        heapq.heapify(ends)
        maxOverlap = 0
        for i in range(len(sIntervals)):

            while(ends and ends[0] <= sIntervals[i].start):
                heapq.heappop(ends)
            
            heapq.heappush(ends, sIntervals[i].end)
            
            maxOverlap = max(maxOverlap, len(ends))
        
        return maxOverlap




        