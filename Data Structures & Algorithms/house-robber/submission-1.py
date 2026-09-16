from functools import lru_cache


class Solution:
    
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def recursive_call(index):
            if index >= len(nums):
                return 0
            return max(nums[index] + recursive_call(index + 2), recursive_call(index + 1))
        return recursive_call(0)