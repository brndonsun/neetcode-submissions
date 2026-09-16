class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for number in nums:
            if number in seen.keys():
                return True
            else:
                seen[number] = 1
        return False