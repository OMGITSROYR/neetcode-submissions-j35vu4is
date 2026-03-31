class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        right = 0
        left = len(s) - 1

        while left >= right:
            if not s[left].isalnum():
                left -= 1
                continue
            if not s[right].isalnum():
                right += 1
                continue
            if s[left] != s[right]:
                return False
            else:
                right += 1
                left -= 1
        
        
        return True

        
        