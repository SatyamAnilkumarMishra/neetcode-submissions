class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' This is the best Optimal Solution
        map = {}
        for i,n in enumerate(nums):
            complement = target - n

            if complement in map:
                return [map[complement],i]

            map[nums[i]] = i '''

        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in map:
                return [map[complement],i]

            map[nums[i]] = i


        
            
        
        
       
                    

                    
        
        
                    
                
        