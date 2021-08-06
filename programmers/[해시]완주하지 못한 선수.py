from collections import Counter
"""
- c 에 없는 p 구해야하는데, 동명이인 있음
- counter 객체 연산 사
"""
def solution(participant, completion):
    answer = ''
    
    p = Counter(participant)
    c = Counter(completion)
    l = list((p-c).keys())
    answer += l[0]

            
    return answer
