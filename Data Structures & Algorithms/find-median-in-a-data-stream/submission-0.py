class MedianFinder:

    def __init__(self):
        self.sHeap = []
        self.lHeap = []
        


    def addNum(self, num: int) -> None:
        
        s = len(self.sHeap)
        l = len(self.lHeap)

        if(s == 0):
            heapq.heappush(self.sHeap, -num)
        
        elif(s-l == 1):

            if(num < -self.sHeap[0]):
                maxS = -heapq.heappop(self.sHeap)
                heapq.heappush(self.lHeap, maxS)
                heapq.heappush(self.sHeap, -num)
            else:
                heapq.heappush(self.lHeap, num)

        elif(l-s == 1):

            if(num > self.lHeap[0]):
                minL = heapq.heappop(self.lHeap)
                heapq.heappush(self.sHeap, -minL)
                heapq.heappush(self.lHeap, num)
            else:
                heapq.heappush(self.sHeap, -num)

        else:

            if(num > -self.sHeap[0]):
                heapq.heappush(self.lHeap, num)
            else:
                heapq.heappush(self.sHeap, -num)


    def findMedian(self) -> float:

        s = len(self.sHeap)
        l = len(self.lHeap)

        if l == 0:

            if self.sHeap:
                return -self.sHeap[0]
            else:
                return None
            
        if s>l:
            
            return -self.sHeap[0]
        if l>s: 
            return self.lHeap[0]
        else:
            return (-self.sHeap[0] + self.lHeap[0])/2
        
        