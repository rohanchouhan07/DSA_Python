class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        for i in range(0,numRows):
            curr=[]
            for j in range(0,i+1): 
                if j==0 or j==i:
                    curr.append(1)
                else:
                    curr.append(arr[i-1][j-1] + arr[i-1][j])

            arr.append(curr)

        return arr