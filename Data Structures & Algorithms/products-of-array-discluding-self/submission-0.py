class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        prefix_product = [0] * len(nums)
        prefix_product[0] = 1
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]

        suffix_product = [0] * len(nums)
        suffix_product[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i + 1]

        for j in range(len(nums)):
            result[j] = suffix_product[j] * prefix_product[j]

        return result
                


            