class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        for i,c in enumerate(zip(*strs)):
            if len(set(c))>1:
                return strs[0][:i]
        return min(strs,key=len)
        
