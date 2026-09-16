class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #idea is for every char in text2 you make the choice to either take the curr
        #character if they match or skip
        len1 = len(text1)
        len2 = len(text2)

        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)] #defines the longest length acheiveable at this index
        

        ind1, ind2 = 0, 0
        for ind1 in range(len1 - 1, -1, -1):
            for ind2 in range(len2 - 1, -1, -1):
                if text1[ind1] == text2[ind2]:
                    dp[ind1][ind2] = 1 + dp[ind1 + 1][ind2 + 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 + 1][ind2], dp[ind1][ind2 + 1])

        return dp[0][0]