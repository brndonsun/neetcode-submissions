class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        for letter in t:
            s_dict[letter] = s_dict.get(letter, 0) - 1
        
        for value in s_dict.values():
            if value != 0:
                return False

        return True