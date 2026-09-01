class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums,L,M,R):
            left , right = nums[L:M+1] , nums[M:R+1]
            i , j ,k = L ,0,0
            while j < len(L) and k < len(R):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j+=1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                nums[i] = left[j]
                j+=1
                i+=1
            
            while k < len(right):
                nums[i] = right[j]
                k+=1
                i +=1

        def mergeSort(arr,l,r):
            if l == r:
                return arr
            
            mid = (l+r) // 2
            mergeSort(nums,l,m)
            mergeSort(nums,m+1,r)
            merge(nums,l,m,r)
            return nums

        return mergeSort(nums,l,m,r)
        