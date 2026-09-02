class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        needs to find a substring only have unique characters
        it needs to be longest substring

        abca --> valid or not
        """

        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If the character is already in our window, 
            # shrink the window from the left until it's removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the new character to our window
            char_set.add(s[right])
            
            # Update the max length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length