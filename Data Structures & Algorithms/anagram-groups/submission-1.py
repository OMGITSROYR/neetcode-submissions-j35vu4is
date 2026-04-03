from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        #loop through strs and make a dict 
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        
        res = [val for val in anagram_map.values()]

        return res