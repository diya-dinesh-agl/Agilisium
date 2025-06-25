class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        return n != len(set(nums))
