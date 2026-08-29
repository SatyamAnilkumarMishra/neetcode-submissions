class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] , nums[i+1] = nums[i+1] , nums[i]
                i += 1
                nums[i].pop()
        return nums

            
        