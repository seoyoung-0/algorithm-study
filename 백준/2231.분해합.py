#2231 분해합

N = int(input())
min_ = N

for i in range(1,N+1):
    each_sum = 0
    each_sum += i
    num = str(i)
    for n in num:
        each_sum += int(n)
        
    if each_sum == N:
        print(i)
        break
        
    if i==N:
        print(0)

###
result = 0 #1부터 증가하면서 최소값 구하는 거니까
# 조건 만족하면 멈추기(최소값 갱신하지 말고)

for i in range(1,N+1):
    a = list(map(int, str(i)))  #숫자 자릿수 쪼개기
    result = i + sum(a)
    
    if result == N:
        print(i)
        break
    
    if i == N:
        print(0)
