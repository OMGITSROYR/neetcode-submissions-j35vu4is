class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window so there's 2 pointers
        # the right pointer stays where it is, and the left pointer expands until a duplicate is found
        # if a duplicate is found then we move the right pointer (shrinking the window)
        # at each iteration we check the length of the window and compare it to the max 
        # have a set to keep track of characters seen 

        if not s:
            return 0

        max_length = 1
        right,left= 1,0
        seen = set()
        seen.add(s[0])

        while(right < len(s)):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                right += 1
                max_length = max(max_length,right-left)
        
        return max_length
            
