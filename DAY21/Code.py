class Solution(object):
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            if(i == 0):
                prev = [1]
                res.append(prev)
            else:
                curr = [1]
                x = 1
                while (x<i):
                    curr.append(prev[x-1]+prev[x])
                    x+=1
                curr.append(1)
                res.append(curr)
                prev = curr
        return res
