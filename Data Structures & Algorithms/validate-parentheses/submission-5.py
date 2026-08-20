class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(',']':'[','}':'{'}
        stack = []

        for c in s:
            if c in brackets.keys():
                if not stack:
                    return False
                temp = stack.pop()
                if temp != brackets[c]:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        
        return True