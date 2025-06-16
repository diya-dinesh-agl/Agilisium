class Solution(object):
    def fourSum(self, nums, target):
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]*4>target:
                break

            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                if nums[j]*3>target-nums[i]:
                    break
                l,r = j+1, n-1
                while l<r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    if s>target:
                        r = r-1
                    elif s<target:
                        l=l+1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l] == nums[l+1]:
                            l=l+1
                        while l<r and nums[r] == nums[r-1]:
                            r=r-1
                        l,r=l+1,r-1
        return res
