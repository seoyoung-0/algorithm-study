# https://leetcode.com/problems/jewels-and-stones/
'''
- 해시테이블로 풀기 
( stone 별 개수 저장 - 보석 별 stone 개수 더하기 )
'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        count = {}
        
        for char in stones:
            
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
        
        sum = 0 
        for char in jewels:
            if char in count.keys():
                sum += count[char]
            else:
                continue
        
        return sum
