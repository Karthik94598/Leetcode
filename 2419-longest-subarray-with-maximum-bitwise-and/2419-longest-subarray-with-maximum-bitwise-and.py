class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Step 1: Find the maximum element in the array
        max_num = max(nums)
        
        # Step 2: Initialize variables for tracking the longest subarray
        longest = 0
        current_length = 0
        
        # Step 3: Traverse through the array and find the longest subarray with max_num
        for num in nums:
            if num == max_num:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0
        
        return longest
