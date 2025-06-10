class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k%n
        r = nums[-k:]
        r.extend(nums[:-k])
        nums[:] = r[:]
        
