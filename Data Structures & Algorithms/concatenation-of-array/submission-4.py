class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

        """
        n = len(nums)
        ans = [0]*(2*n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        
        return ans """

        """
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[i])

        for i in range(n):
            ans.append(nums[i])

        return ans """

 



  




        

        
        