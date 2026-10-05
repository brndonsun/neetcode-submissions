class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #three cases: either add some new paren on each side
        # (prev_result) 
        #or 
        # add right next to it
        # prev_result ()
        # () prev_result

        res = []
        def dfs(curr_open, curr_close, result):
            if len(result) == 2 * n:
                res.append(result)
                return
            if curr_open < n:
                dfs(curr_open + 1, curr_close, result + '(')
            if curr_open > curr_close:
                dfs(curr_open, curr_close + 1, result + ')')
            return

        dfs(0, 0, "")
        return res