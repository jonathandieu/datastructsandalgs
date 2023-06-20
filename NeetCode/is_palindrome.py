def is_palindrome(s: str) -> bool:
    """
    Given a string sequence, determines whether or not it's a palindrome
    """
    pass

def parse_string(s: str) -> bool:
    """
    Given a string sequence, returns string without whitespaace and punctuation.
    """
    return [char for char in s if char.isalpha()].join()