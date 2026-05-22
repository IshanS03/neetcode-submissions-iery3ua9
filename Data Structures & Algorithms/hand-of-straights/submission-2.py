class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
            
        groups = []
        sHand = sorted(hand)
        frequencies = {}
        for num in hand:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        for num in sHand:
            if frequencies[num]:
                for i in range(num, num + groupSize):
                    if frequencies.get(i, 0) == 0:
                        return False
                    frequencies[i] -= 1
            
        return True