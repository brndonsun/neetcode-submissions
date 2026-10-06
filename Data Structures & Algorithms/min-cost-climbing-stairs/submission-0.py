class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp[i] is the min cost to get to this step
        n = len(cost) + 1
        #recurrence is the current step = the minimum of either the step 1
        #down or 2 down
        dp = [0] * n
    
        for i in range(2, n):

            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n - 1]


