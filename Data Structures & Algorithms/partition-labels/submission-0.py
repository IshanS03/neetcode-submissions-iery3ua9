class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        freq = Counter(s)
        curSub = set()
        length = 0 
        res = []
        for c in s:

            length += 1
            freq[c] -= 1
            curSub.add(c)

            if freq[c] == 0:
                curSub.remove(c)
                if not curSub:
                    res.append(length)
                    length = 0
            
        
        return res