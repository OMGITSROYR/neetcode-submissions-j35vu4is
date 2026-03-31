from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        k_map = defaultdict(int)
        result = []

        for i in nums:
            k_map[i] += 1
        
        for _ in range(k):
            max_freq = -1
            max_index = None
            
            for num,freq in k_map.items():
                if freq > max_freq:
                    max_freq = freq
                    max_index = num
            result.append(max_index)
            del k_map[max_index]

        return result 

        



        