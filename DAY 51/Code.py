class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        n = 1
        for val in target:
            while n<val:
                res+=["Push","Pop"]
                n+=1
            res.append("Push")
            n+=1
        return res
