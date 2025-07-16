class Solution(object):
    def majorityElement(self, nums): 
        c, v = 0, None
        for x in nums: 
            if c == 0: v = x
            c += 1 if x == v else -1
        return v
