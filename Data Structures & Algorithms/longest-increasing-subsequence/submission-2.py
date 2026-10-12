class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        dp = [1] * len(nums)

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)


        return max(dp)