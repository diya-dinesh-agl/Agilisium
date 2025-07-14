class Solution(object):
    def subsetsWithDup(self, nums):
        res = [[]]
        for n in sorted(nums):
            res += [r + [n] for r in res if r + [n] not in res]
        return res
