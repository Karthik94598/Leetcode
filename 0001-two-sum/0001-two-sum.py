class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                x=nums[i]+nums[j]
                if x == target:  
                    return[i,j]
        return[]