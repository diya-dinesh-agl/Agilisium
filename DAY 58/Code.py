class Solution:
    def longestValidParentheses(self, s):
        a, r = [-1], 0
        for i, c in enumerate(s):
            if c == '(': a.append(i)
            else:
                a.pop()
                if not a: a.append(i)
                else: r = max(r, i - a[-1])
        return r
