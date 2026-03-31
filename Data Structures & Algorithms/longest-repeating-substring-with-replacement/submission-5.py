from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0
        string_map = defaultdict(int)
        left = 0
        max_window_size = 0
        max_freq = 0

        for right in range(len(s)):
            #size of the sliding window
            window_size = right - left + 1
            #append the current element to the window
            string_map[s[right]] += 1
            # highest value
            max_freq = max(string_map.values())
            
            # if the window size is smaller than the number of possible replacements; move left pointer up
            # window_size - max_freq is the amount of replacements available
            while window_size - max_freq > k and left <= right:
                string_map[s[left]] -= 1
                left += 1
                window_size = right - left + 1

            max_window_size = max(max_window_size,((right - left) + 1))

        return max_window_size
