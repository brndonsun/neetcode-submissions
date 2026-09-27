class Solution:
    def longestPalindrome(self, s: str) -> str:
        #intution: from each spot expand from middle and check for even and odd palidromes

        best_start = 0
        best_length = 0
        n = len(s)

        for i in range(n):
            #odd
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > best_length:
                    best_start = l
                    best_length = r - l + 1
                l -= 1
                r += 1

            #even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > best_length:
                    best_start = l
                    best_length = r - l + 1
                l -= 1
                r += 1
            
        return s[best_start : best_start + best_length]

