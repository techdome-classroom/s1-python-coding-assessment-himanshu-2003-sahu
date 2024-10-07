def decode_message(s: str, p: str) -> bool:
    def match_helper(s_idx, p_idx):
        # Base case: If both the message and pattern are fully processed, return True
        if s_idx == len(s) and p_idx == len(p):
            return True
        # If the pattern is exhausted but the message is not, or vice versa, return False
        if p_idx == len(p):
            return False

        # Case 1: Handle '*' in the pattern
        if p[p_idx] == "*":
            # Two possibilities:
            # 1. '*' matches no characters (move to the next pattern character)
            # 2. '*' matches one or more characters (move to the next message character)
            return match_helper(s_idx, p_idx + 1) or (
                s_idx < len(s) and match_helper(s_idx + 1, p_idx)
            )

        # Case 2: Handle '?' or matching specific characters
        if s_idx < len(s) and (p[p_idx] == "?" or p[p_idx] == s[s_idx]):
            # Move to the next character in both message and pattern
            return match_helper(s_idx + 1, p_idx + 1)

        # If characters don't match and it's not a wildcard situation, return False
        return False

    # Start the matching process from index 0 for both the message and the pattern
    return match_helper(0, 0)


# Test cases
print(decode_message("aa", "a"))  # False
print(decode_message("aa", "*"))  # True
print(decode_message("cb", "?a"))  # False
print(decode_message("abc", "a*c"))  # True
print(decode_message("abc", "a?c"))  # True
