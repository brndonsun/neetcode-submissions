class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dictionary = {}
        t_dictionary ={}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in s_dictionary.keys():
                s_dictionary[s[i]] += 1
            else:
                s_dictionary[s[i]] = 1
            if t[i] in t_dictionary.keys():
                t_dictionary[t[i]] += 1
            else:
                t_dictionary[t[i]] = 1
            
        return s_dictionary == t_dictionary