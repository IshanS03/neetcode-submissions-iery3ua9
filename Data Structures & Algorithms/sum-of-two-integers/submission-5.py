class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        MAX = 2 ** 31 - 1

        res = 0
        carry = 0
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        for i in range(32):
            bit_a = a & 1
            bit_b = b & 1
            bit = bit_a ^ bit_b ^ carry
            res |= bit << i
            carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))
            a = a >> 1
            b = b >> 1
            
        
        if res > MAX:
            res -= 2**32
        return res
