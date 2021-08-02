# https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
: 중복되지 않는 문자열 중 가장 긴 문자열
- 슬라이딩 윈도우
- 중복 나오면, start 인덱스 = 기존의 중복 대상 +1 
- ** start 가 기존의 중복 대상보다 크면 길이 갱신 
- input = "tmmzuxt" -> 마지막 문자 - used['t'] 값 변경 후, 길이 갱신해야하니까
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len = 0 
        start = 0 

        for index, char in enumerate(s):

            if char in used and start <= used[char]:
                start = used[char] + 1

            else:
                max_len = max(max_len, index - start + 1)

            used[char] = index

        return max_len
        
