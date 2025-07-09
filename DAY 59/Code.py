class Solution(object):
    def isValid(self, s):
        S, M = [], {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in M:
                if not S or S.pop() != M[c]: return False
            else: S += c,
        return not S
