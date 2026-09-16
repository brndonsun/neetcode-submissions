class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        freq = {}
        l = 0
        most_freq = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

            most_freq = max(most_freq, freq[s[i]])
            while (i - l + 1) - most_freq > k:
                freq[s[l]] -= 1
                l += 1

            result = max(result, i - l + 1)

        return result