class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(ind, curr_combination, curr_total):
            if ind >= len(candidates):
                return

            if candidates[ind] + curr_total > target:
                return
            elif candidates[ind] + curr_total == target:
                result.append(curr_combination + [candidates[ind]])
                return
            else:
                
                dfs(ind + 1, curr_combination + [candidates[ind]], curr_total + candidates[ind])
            while ind + 1 < len(candidates) and candidates[ind] == candidates[ind + 1]:
                ind += 1
            dfs(ind + 1, curr_combination, curr_total)


        
        dfs(0, [], 0)
        return result

