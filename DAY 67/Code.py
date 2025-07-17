class Solution:
    def findLHS(self, a: List[int]) -> int:
        return (z:=Counter(a)) and max(z[v+1] and z[v]+z[v+1] for v in z)
