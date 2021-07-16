# https://leetcode.com/problems/reverse-string/

'''
Write a function that reverses a string. 
The input string is given as an array of characters s.
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s)-1
        for w in range(len(s)):
            if start >= end:
                break
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
