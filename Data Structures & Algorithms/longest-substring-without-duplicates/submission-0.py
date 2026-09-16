class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        string_map = set()
        for r in range(len(s)):
            while s[r] in string_map:
                string_map.remove(s[l])
                l += 1
            string_map.add(s[r])
            max_len = max(max_len, (r - l + 1))

        return max_len

