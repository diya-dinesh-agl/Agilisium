class Solution(object):
    def isMatch(self, s, p):
        i,j = 0,0
        lm ,star = 0,-1

        while i < len(s):
            if j<len(p)  and (s[i]==p[j] or p[j]=="?"):
                i+=1
                j+=1
            elif j< len(p) and p[j] == "*":
                lm = i
                star = j
                j+=1
            elif star!=-1:
                j = star+1
                i = lm+1
                lm+=1
            else:
                return False
        while j<len(p) and p[j] == "*":
            j+=1
        return j == len(p)
