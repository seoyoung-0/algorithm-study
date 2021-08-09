# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
         }
        
        def dfs(index, word):
            if len(word) == len(digits):
                res.append(word)
                return
            for i in range(index,len(digits)):
                for w in graph[digits[i]]:
                    dfs(i + 1, word + w)
        
        if digits is "":
            return []
        
        res = []
        dfs(0,"")
        return res
