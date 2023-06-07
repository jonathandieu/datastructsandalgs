class Codec:
    def encode(self, strs: list[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        pass


    def decode(self, s: str) -> list[str]:
        """
        Decodes a single string to a list of strings.
        """
        pass



# The Codec object will be instantiated and called as such:
strs = ["str1", "str2", "str3"]
codec = Codec()
codec.decode(codec.encode(strs))
