# 네트워크 선 자르기
# 1m, 2m 로 자르는 방법 ( 4m 선이 주어진다면 )
# 7m 라면 몇가지?

n = int(input())

### bottom-up
res = [0] * (n+1)

res[1],res[2] = 1,2  # 전체가 1m,2m 일때 각각 1가지, 2가지
for i in range(3, n+1):
    res[i] = res[i-1] + res[i-2]
print(res)
print(res[n])


### top-down_재귀
# save 에 이미 알고있는 값 가지치기 *****

def dfs(len):
    if save[len]:
        return save[len] #기록해둔거 활용해야한다 꼭 *****
    
    if len == 1 or len == 2:
        return len
    else:
        save[len] = dfs(len-1) + dfs(len-2)
        return save[len]

save = [0] * (n+1)
print('dfs',dfs(n))
