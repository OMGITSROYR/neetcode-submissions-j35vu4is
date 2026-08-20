class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        s = s.lower()

        while(right >= left):
            if not s[right].isalnum():
                right -= 1
                continue

            if not s[left].isalnum():
                left += 1
                continue

            if s[right] != s[left]:
                return False
            
            right -= 1
            left += 1

        return True
        