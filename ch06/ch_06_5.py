# https://leetcode.com/problems/group-anagrams/
'''
49.
동일 문자로 구성된 애너그램 그룹화
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = collections.defaultdict(list)

        for word in strs:

            # 단어 sorted -> 문자 하나씩 정렬
            # 키값이 동일한 문자, value 가 단어들 !

            ana[''.join(sorted(word))].append(word)
            # print(ana)

        return ana.values()
