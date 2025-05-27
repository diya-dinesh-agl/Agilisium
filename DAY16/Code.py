from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
        subs = Counter(s)
        d = subs[s[0]]
        for i in subs.values():
            if i != d:
                return False
        return True
