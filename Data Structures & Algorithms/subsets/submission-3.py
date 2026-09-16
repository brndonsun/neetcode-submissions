from functools import lru_cache

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        
        def dfs(curr, i):
            if i == len(nums):
                result.append(curr)
                return

            array_copy = curr.copy()
            array_copy.append(nums[i])
            dfs(array_copy, i + 1)
            dfs(curr, i + 1)
            


        
        dfs([], 0)

        return result
        