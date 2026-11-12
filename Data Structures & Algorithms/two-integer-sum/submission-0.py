class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i,v in enumerate(nums):
            if (target - v) in result:
                return [result[target-v], i]
            else: 
                result[v] = i