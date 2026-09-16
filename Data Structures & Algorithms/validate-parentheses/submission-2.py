class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_pair = {'}': '{', ')': '(',']': '['}
        stack = []
        for p in s:
            if p in ('{', '(', '['):
                stack.append(p)
            else:
                if len(stack) == 0 or parentheses_pair[p] != stack.pop():
                    return False

        return (len(stack) == 0)