from collections import deque
'''
- deque 는 연결리스트 : popleft, append 자유롭게 사용해도 연결
- popleft랑 max의 우선순위 비교 - 작으면 맨 뒤로 !!! <- 앞에 순서 달라지는 거 해결가능
- 우선순위 안 작으면, answer 증가
'''
def solution(priorities, location):
    answer = 0
    
    deq = deque((v,i) for i,v in enumerate(priorities))
    # 우선순위 값, 인덱스 저장
    
    while deq:
        item = deq.popleft()
        if len(deq)!=0:
            
            if item[0] < max(deq)[0]: # 우선순위 더 작으면
                deq.append(item) # 맨 뒤에 다시 넣기
            else:
                answer += 1
                if item[1] == location:
                    break
        else:
            answer += 1
            if item[1] == location:
                break
                
    return answer
    
    
    '''
# 우선순위 max 기준 앞뒤 나눠서 정렬하고 합치기 
# ..예제만 됨

    max_split = max(deq)
    post, prev = [],[]
    for i in range(len(deq)):
        if deq[i][1] >= max_split[1]:
            post.append(deq[i])
        else:
            prev.append(deq[i])
    post = sorted(post, key=lambda x:x[0],reverse=True)
    print(post)
    prev = sorted(prev, key = lambda x:x[0],reverse=True)
    print(prev)
    
    res = post + prev
    for r in range(len(res)):
        if res[r][1] == location:
            answer = r+1
    '''
