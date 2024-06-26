class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        x=len(nums1)
        if x%2 == 0:
            y = x//2
            z = (nums1[y]+nums1[(y-1)])/2
            return z
        else:
            y = x//2
            return nums1[y]
        