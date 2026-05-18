class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total = 0
        start = 0
        curTotal = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curTotal += gas[i] - cost[i]
            if curTotal < 0:
                start = i + 1
                curTotal = 0
            
        if total < 0:
            return -1
        else:
            return start

