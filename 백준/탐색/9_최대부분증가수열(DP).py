# 최대 부분 증가수열(DP)
# ex) 2 7 5 8 6 4 7 12 3
# ( 2 5 6 7 12 ) 로 5개가 최대 길이

# 1. 각 요소가 마지막자리일 때의 경우수 dy 저장
# 2. 자기보다 앞에 있고, 작은 수의 dy 중 최대값 + 1 이 dy 값
#  ** 자기보다 작은 수 중 경우의 수 제일 많은거에 붙여야 하니까 

N = int(input())
num = list(map(int, input().split()))
num.insert(0,0)
dy = [0] * (N+1)
dy[1] = 1

for i in range(2, N+1):
    pre_max = 0 
    for j in range(i-1, 0, -1): # 앞으로
        if num[j] < num[i]:
            pre_max = max(pre_max, dy[j])
        
    dy[i] = pre_max + 1
    
print(max(dy))
