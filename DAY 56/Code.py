class Solution(object):
    def wordBreak(self, s, w):
        w,memo = set(w),{}
        def f(i):
            if i == len(s): return [""]
            if i in memo: return memo[i]
            memo[i] = [s[i:j]+(" "+k if k else "") for j in range(i+1,len(s)+1) if s[i:j] in w for k in f(j)]
            return memo[i]
        return f(0)
