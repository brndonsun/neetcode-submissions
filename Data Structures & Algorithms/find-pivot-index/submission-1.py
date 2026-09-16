class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i-1] + nums[i-1]

        for i in range(length):
            leftSum = prefix[i]
            rightSum = prefix[length] - prefix[i + 1]
            if leftSum == rightSum:
                return i

        return -1
