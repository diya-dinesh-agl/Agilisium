class Solution:
    def convert(self, s: str, r: int) -> str:
        if r == 1: return s
        z = ['']*r
        i,d = 0,1
        for c in s:
            z[i] += c
            i += d
            if i ==0 or i==r-1:d*=-1
        return ''.join(z)
