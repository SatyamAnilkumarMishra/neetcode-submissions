class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0 
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                return True
                i+=1
            else:
                return False
        
        
        