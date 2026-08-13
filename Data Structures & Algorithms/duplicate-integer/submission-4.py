class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        unique_element = set(nums)
        if len(unique_element) != n:
            return True
        return False

        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False

        
        
        
        