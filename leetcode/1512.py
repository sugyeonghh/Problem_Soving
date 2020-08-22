class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for i, data1 in enumerate(nums):
            for j, data2 in enumerate(nums):
                if data1==data2 and i<j:
                    result += 1
        return result