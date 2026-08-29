class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        for i in range(n-1):
            if nums[i] == val:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                i += 1
        return nums




        