class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        x = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[x] = nums[i]
                x = x+1
        return x 
