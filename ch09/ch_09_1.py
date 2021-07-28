# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        first = ['(','[','{']
        second = [')',']','}']
        
        for char in s:
            if char in first:
                stack.append(char)
            elif char in second:
                if stack: 
                # pop 하기 전에는 비어있는지 꼭 확인
                    popp = stack.pop()
                    if first.index(popp)==second.index(char):
                        continue
                    else:
                        return False
                else:
                    return False
            
        if stack:
        # 스택에 남아있는지 확인
            return False
            
        return True

    
        ''' 키-value 형태로 짝 지어주기
        stack = []
        table = {
            ')':'(',
            ']':'['.
            '}':'{',
        }
        
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        
        return len(stack) == 0
        
        '''
