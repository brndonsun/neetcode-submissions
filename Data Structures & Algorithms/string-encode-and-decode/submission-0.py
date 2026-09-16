class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + "*" + string
        return encoded_str



    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        curr_len = ""
        read_string = False
        i = 0

        while i < len(s):
            if s[i] != "*":
                curr_len += s[i]
                i += 1
            else:
                curr_string_builder = ""
                for j in range(int(curr_len)):
                    curr_string_builder += (s[j + i + 1])

                decoded_strings.append(curr_string_builder)
                i = i + int(curr_len) + 1
                curr_len = ""

        return decoded_strings





