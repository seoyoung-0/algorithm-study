'''
[프로그래머스]
스택/큐 - 기능개발
'''
import math

def solution(progresses, speeds):
    days = [0]*len(progresses)
    answer=[]

    # 걸리는 날짜 리스트 구하기
    for i, p in enumerate(progresses):
        diff = 100 - p
        day = math.ceil(diff / speeds[i])
        days[i] = day

    days.reverse()
    print(days)

    sum = 1
    max = days.pop()
    while days:

        if days[-1] > max:
            answer.append(sum)
            sum = 1
            max = days.pop()

        else:
            sum += 1
            days.pop()

        if len(days)==0:
            answer.append(sum)
    
    return answer
