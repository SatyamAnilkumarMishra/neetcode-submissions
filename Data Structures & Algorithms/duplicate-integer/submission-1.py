class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0 
        for j in range(0,len(nums)-1):
            if nums[j] == nums[i]:
                i+=1
                return True
                
           
            return False
        
        
        