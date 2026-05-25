class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resLen = 0
        res = 0
        for i in range(len(s)):

            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = l 
                    resLen = r - l + 1
                l -= 1
                r += 1  
            
            
            r = i+1
            l = i

            while l >= 0 and r< len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = l
                    resLen = r - l + 1
                    print(resLen, "even")
                l -= 1
                r += 1
            
        return s[res:res+resLen]
            



       