class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = [False] * (len(s) + 1)
        # dp[len(s)] = True

        # for i in range(len(s) - 1, - 1, -1):
        #     for w in wordDict:
        #         if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
        #             dp[i] = dp[i + len(w)]    
        #             print(i, i+len(w), s[i: i + len(w)])
        #         if dp[i]:
        #             break
        
        # print(dp)
        # return dp[0]

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for w in wordDict:
                if (i - len(w)) >= 0 and s[i - len(w): i] == w:
                    dp[i] = dp[i - len(w)]    
                    print(i, i-len(w), s[i - len(w): i], dp[i])
                if dp[i]:
                    break

        
        print(dp)

        return dp[len(s)] 