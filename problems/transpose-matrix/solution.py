import numpy as np
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        df=np.array(matrix)
        return(df.T.tolist())