class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1): #start, stop, step
            if nums[i] + i >= goal:
                goal = i

        return goal == 0