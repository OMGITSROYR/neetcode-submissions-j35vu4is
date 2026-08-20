class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # iterate through each and add to a set and expand
        # if char in set, shrink the window
        # keep track of the max
        if not s:
            return 0
        if len(s) == 1:
            return 1

        res = 0
        right = 1
        left = 0
        unique = set()
        unique.add(s[left])

        while(right < len(s)):
            if s[right] in unique:
                unique.remove(s[left])
                left += 1
                continue
            
            unique.add(s[right])
            res = max(res,len(unique))
            right += 1

        return res
        