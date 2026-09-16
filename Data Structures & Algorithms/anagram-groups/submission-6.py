class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dictionary = defaultdict(list)
        for string in strs:
            letter = 26 * [0]
            for char in string:
                letter[ord(char) - ord("a")] += 1
            result_dictionary[tuple(letter)].append(string)

        return list(result_dictionary.values())