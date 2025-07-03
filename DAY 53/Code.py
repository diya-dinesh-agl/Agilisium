class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws, n = set(wordDict), len(s)
        dp = [False]*(n+1)
        dp[n] = True
        for i in range(n-1,-1,-1):
            dp[i]=any(s[i:j] in ws and dp[j] for j in range(i+1,n+1))
        return dp[0]
