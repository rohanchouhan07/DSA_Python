class Solution:
    def checkString(self, s: str) -> bool:
        return s.rfind('a') < s.find('b') or s.find('b')==-1
        # sort=sorted(s)
        # ans="".join(sort)
        # return s==ans


        