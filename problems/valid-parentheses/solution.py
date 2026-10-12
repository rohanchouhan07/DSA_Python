class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for x in s:

            if x in '{([':
                stack.append(x)

            elif x==')':
                if( len(stack) != 0 and stack[-1]=='('):
                    stack.pop()
                else :
                     return False
            elif x==']':
                if(len(stack)!=0 and stack[-1]=='['):
                    stack.pop()
                else :
                     return False
            elif x=='}':
                if(len(stack)!=0 and stack[-1]=='{'):
                    stack.pop()
                else :
                     return False
        return len(stack)==0