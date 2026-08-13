class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        res = 0
        blocks = 0
        while r < len(height):

            if height[r] >= height[l]:
                width = r - l - 1
                res += (width * min(height[l], height[r]))
                res -= blocks
                l = r
                blocks = 0
            else:
                blocks += height[r]

            r += 1

        # backward pass
        i, j = len(height) - 1, len(height) - 2
        blocks = 0
        while j >= l:

            if height[j] >= height[i]:
                width = i - j - 1
                res += (width * min(height[i], height[j]))
                res -= blocks
                i = j
                blocks = 0
            else:
                blocks += height[j]

            j -= 1

        return res


            


