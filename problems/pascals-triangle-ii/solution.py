class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for i in range(1, rowIndex + 1):
            result.append(result[-1] * (rowIndex - i + 1) // i)
        return result