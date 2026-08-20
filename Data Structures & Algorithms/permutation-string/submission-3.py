class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initialise a window the size of s1
        # keep a dict of the freq of the s1 letters
        # substract the letters from the window
        # if hash is empty return true
        if len(s1) > len(s2):
            return False

        freq = defaultdict(int)
        for c in s1:
            freq[c] += 1

        start = 0 
        stop = len(s1) - 1

        while(stop <= len(s2)-1):
            temp = s2[start:stop+1]
            temp_hash = freq.copy()
            for c in temp:
                temp_hash[c] -= 1

            if all(v == 0 for v in temp_hash.values()):
                return True

            start += 1
            stop += 1

        return False
            
        