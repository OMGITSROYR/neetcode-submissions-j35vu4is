class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1

        while(j < len(numbers)):
            value = numbers[i] + numbers[j]

            if value == target:
                return [i+1,j+1]
            elif value < target:
                j += 1
                i += 1
            elif value > target:
                i -= 1
