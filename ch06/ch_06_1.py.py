# https://leetcode.com/problems/valid-palindrome/
'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.replace(' ','')
        s = s.lower()
        st = list(s)
        fin = []
        for word in st:
            if word.isalnum():
                fin.append(word)

        fin2 = fin[::-1]
        d1 = d2 =""

        for i in range(len(fin)):
            d1+=str(fin[i])
        for j in range(len(fin2)):
            d2 += str(fin2[j])

        if d1 == d2:
            return True
        else:
            return False
