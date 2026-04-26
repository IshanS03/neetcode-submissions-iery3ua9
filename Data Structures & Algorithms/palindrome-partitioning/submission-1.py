class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        sub = []
        def dfs(i, j):

            if i >= len(s):
                if i == j:
                    res.append(sub.copy())
                return  

            if(self.isPalindrome(s, j, i)):
                sub.append(s[j: i+1])
                dfs(i+1, i+1)
                sub.pop()
                
            dfs(i+1, j)

        dfs(0, 0)
        return res

    def isPalindrome(self, s, l, r):

        while(l < r):

            if (s[l] != s[r]):
                return False
            l += 1
            r -= 1

        return True

       