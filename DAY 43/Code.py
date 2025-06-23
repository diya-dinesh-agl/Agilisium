class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        cnt = 0
        n = len(s)
        for i in range(n,0,-1):
            if s[i-1] == " ":
                break
            cnt=cnt+1
        return cnt
        
