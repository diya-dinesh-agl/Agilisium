class Solution(object):
    def findMin(self, A):
        l,r = 0,len(A)-1
        while l<r:
            m=(l+r)//2
            if A[m]>A[r]:l = m+1
            else: r = m
        return A[l]
        
