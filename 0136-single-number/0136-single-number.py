class Solution:
    def singleNumber(self, nums):
        nums.sort()  # Sorting the list
        i = 0
        for j in range(i + 1, len(nums), 2):
            if nums[i] == nums[j]:
                i += 2
        return nums[i]
