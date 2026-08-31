class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        N1, N2, N3 = len(s1), len(s2), len(s3)
        N = min(N1, N2, N3)
        finalLength = 0
        for i in range(0, N):
            if s1[i] == s2[i] and s2[i] == s3[i]:
                finalLength += 1
            else:
                break
        if finalLength == 0:
            return -1
        ans = N1 - finalLength
        ans += N2 - finalLength
        ans += N3 - finalLength

        return ans