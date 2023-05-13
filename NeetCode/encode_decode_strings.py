class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """


    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """



# The Codec object will be instantiated and called as such:
strs = ["str1", "str2", "str3"]
codec = Codec()
codec.decode(codec.encode(strs))
