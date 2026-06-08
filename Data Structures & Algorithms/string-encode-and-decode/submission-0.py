class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += word[::-1] + "*@"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        parts = s.split("*@")
    # drop trailing empty if it’s just from the final delimiter
        if parts and parts[-1] == "":
            parts = parts[:-1]
        return [word[::-1] for word in parts]


