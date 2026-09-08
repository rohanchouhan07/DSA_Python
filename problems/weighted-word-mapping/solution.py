class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        """
        List of words
        weights of each character
        find weights for each word
        map the weight with a character
        concatenate all the character and return it
        [1,2,3,4...]
        "abcd" --> 1+2+3+4 = 10
        "abcdefghijklmnopqrstuvwxyz"
        "zyxwvutsrqponmlkjihgfedcba"
        """
        s = "zyxwvutsrqponmlkjihgfedcba"
        ans = ""
        #print(ord('A'))
        def findWeight(word):
            val = 0
            for w in word:# c --> 99 - 97 = 2
                index = ord(w) - ord('a')
                val += weights[index]
            return val%26
        for word in words:
            val = findWeight(word)
            ans += s[val]
        return ans