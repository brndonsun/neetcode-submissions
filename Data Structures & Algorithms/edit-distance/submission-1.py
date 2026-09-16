class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #for each letter, explore the possibility that you insert, delete, or replace
        result = 0
        i, j = 0, 0
        word1_length, word2_length = len(word1), len(word2)

        dp = [[float("inf")] * (word2_length + 1) for i in range(word1_length + 1)]

        for i in range(word1_length + 1):
            dp[i][word2_length] = word1_length - i
        for j in range(word2_length + 1):
            dp[word1_length][j] = word2_length - j

        for i in range(word1_length - 1, -1, -1):
            for j in range(word2_length - 1, -1, -1):
                if word1[i] == word2[j]: 
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i+1][j+1], dp[i][j+1]) + 1


        return dp[0][0]