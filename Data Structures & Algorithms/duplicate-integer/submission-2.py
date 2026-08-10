class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_element = set(nums)
        if len(unique_element) != len(nums):
            return True
        else :
            return False
        
        
        
        