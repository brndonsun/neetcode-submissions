from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2: return False

        for letter in s1:
            s1_freq[letter] += 1

        for i in range(n1 - 1):
            s2_freq[s2[i]] += 1

        l, r = 0, n1 - 1
        while r < n2:
            s2_freq[s2[r]] += 1

            if s1_freq == s2_freq:
                return True
            s2_freq[s2[l]] -= 1
            if s2_freq[s2[l]] == 0:
                s2_freq.pop(s2[l], None)
            l += 1
            r += 1
 
        return False