# https://leetcode.com/problems/longest-palindromic-substring/
'''
5.Given a string s, return the longest palindromic substring in s.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left: int, right: int)-> str:
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left+1:right]

        
        # 단순 예외 처리
        if len(s)<2 or s == s[::-1]: 
            return s

        
        result = ''
        # 3개, 2개 의 투 포인터 이동
        for i in range(0, len(s)-1):
            result = max(result,
                        expand(i,i + 1),
                        expand(i,i + 2),
                        key = len) # max 도 key 요소 사용
        return result
