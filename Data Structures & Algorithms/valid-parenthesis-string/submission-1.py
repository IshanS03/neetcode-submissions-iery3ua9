class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = deque()
        star = deque()
        ast = 0
        r = 0

        for i, c in enumerate(s):

            if c == '(':

                stack.append(i)

            elif c == '*':

                star.append(i)

            else:
                
                if not stack and not star:
                    return False 
                
                if stack:
                    stack.pop()
                else:
                    star.pop()

        while stack and star:
            if stack.pop() > star.pop():
                return False

        return not stack 
