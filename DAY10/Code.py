class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        res = []
        start = end = 0
        nums.append(nums[-1])
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                end = end+1
            else:
                if start<end:
                    res.append(str(nums[start])+"->"+str(nums[end]))
                else:
                    res.append(str(nums[start]))
                start = end = i+1
        return res




        
