class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        newSet = set()

        for item in nums:
            if item not in newSet:
                newSet.add(item)
                
            else:
                return True
        
        return False
        
        