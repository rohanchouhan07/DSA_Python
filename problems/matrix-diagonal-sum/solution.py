class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        sumD = 0
        for i in range(0, N):#Primary
            sumD += mat[i][i] #0,0 | 1,1 | 2,2
        
        for i in range(0, N):#secondary
            sumD += mat[i][N-i-1]

        if N%2 != 0:
            mid = N//2
            sumD -= mat[mid][mid]

        return sumD