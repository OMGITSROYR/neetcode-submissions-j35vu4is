class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        first_word = strs[0]
        if not first_word:
            return ""
        curr = first_word[0]
        diff = False
        if not curr:
            return ""

        while not diff:
            for i in range(len(strs)):
                word = strs[i]
                prefix = word[:len(curr)]

                if prefix != curr:
                    diff = True
                    return first_word[:len(curr)-1]

            if len(curr) == len(first_word):
                return first_word
            curr = first_word[:len(curr) + 1]