class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        f=0
        s=0
        while len(word1)>f and len(word2) > s:
            res+=(word1[f])
            res+=(word2[s])
            f+=1
            s+=1
        while len(word1) > f:
            res+=word1[f]
            f+=1
        
        while len(word2) > s:
            res+=word2[s]
            s+=1
        
        return res