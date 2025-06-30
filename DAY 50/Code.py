class Solution:
    def longestPalindrome(self, s: str) -> str:
        def long(left,right):
            while left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return s[left+1:right]
        longest = ""

        for i in range(len(s)):
            odd_pal = long(i,i)
            even_pal = long(i,i+1)
            longest = max(longest, odd_pal, even_pal, key = len)
        return longest
    
