class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1,n-1):
            for j in range(2,n):
                if nums[j] > nums[i]:
                    i += 1
                    j += 1
                    return
                nums[j] , nums[i] = nums[i] , nums[j]
            
        nums[i]
          

        