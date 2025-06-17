class Solution(object):
    def solveNQueens(self, n):
        def QueenSearch(queens,diff,summ):
            x = len(queens)
            if x == n:
                res.append(queens)
                return None
            for y in range(n):
                if y not in queens and x-y not in diff and x+y not in summ:
                    QueenSearch(queens+[y], diff+[x-y], summ+[x+y])

        res= []
        QueenSearch([],[],[])
        return [["."*i + "Q"+"."*(n-i-1) for i in z] for z in res]
