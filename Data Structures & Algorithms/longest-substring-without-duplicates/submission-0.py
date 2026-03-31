from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left_pointer = 0
        
        string_map = defaultdict(int)

        for c in range(len(s)):
            string_map[s[c]] += 1
            while string_map[s[c]] > 1:
                left_pointer += 1
                string_map[s[left_pointer - 1]] -= 1
            result = max(c - left_pointer + 1,result)

        return result

            



            
