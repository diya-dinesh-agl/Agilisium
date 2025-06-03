class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for i in columnTitle:
            result = result*26+(ord(i)-64)
        return result
