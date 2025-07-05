class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = sorted(nums1+nums2)
        n = len(x)
        return (x[n//2]+x[~(n//2)])/2
