class Solution:
    def isPalindromic(self, s: str) -> bool:
        # Step 1: Convert every character to an 8-bit padded binary string
        binary_string = "".join(f"{ord(c):08b}" for c in s)
        
        # Step 2: Check if the string reads the same forwards and backwards
        return binary_string == binary_string[::-1]