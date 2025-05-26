class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def is_palindrome(s):
            return s == s[::-1]

        word_dict = {word[::-1]: i for i, word in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            for j in range(len(word)+1):
                pref = word[:j]
                suff = word[j:]

                if is_palindrome(pref):
                    idf = word_dict.get(suff)
                    if idf is not None and idf != i:
                        res.append([idf,i])
                if j!=len(word) and is_palindrome(suff):
                    idf = word_dict.get(pref)
                    if idf is not None and idf != i:
                        res.append([i,idf])
        return res



