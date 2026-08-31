class Solution:
    def checkString(self, s: str) -> bool:
        sort=sorted(s)
        ans="".join(sort)
        if s==ans:
            return True
        else:
            return False
        