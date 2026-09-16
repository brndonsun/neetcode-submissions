class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #intuition: two pointer after sorting
        n = len(nums)
        nums.sort()

        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # -num[i] = nums[j] + nums[k]
            target = -nums[i]
            #two pointer
            r = n - 1
            l = i + 1
            while l < r:
                if nums[r] + nums[l] == target:
                    result.append([nums[i], nums[r], nums[l]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[r] + nums[l] > target:
                    r -= 1
                else:
                    l += 1

        return result

