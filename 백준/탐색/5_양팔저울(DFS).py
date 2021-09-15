# 3.양팔저울
# 추 무게 + 물쪽에도 추 놓기(==sum에서 빼기)
# 추 무게에 추가 / 물 무게에 추가 / 추 사용 x
# ex) 추 무게 =(1,5,7) -> 11가지 측정 가능

def dfs(remain, sub_sum):
    
    if sub_sum > 0 and sub_sum not in res:
        res.append(sub_sum)
    if sub_sum == s:
        return
    
    for i,n in enumerate(remain):
        
        dfs(remain[i+1:], sub_sum + n)
        dfs(remain[i+1:], sub_sum - n)
        dfs(remain[i+1:], sub_sum)

k = int(input())
weight = list(map(int, input().split()))
s = sum(weight)
sub_sum = 0
res = []
dfs(weight, 0)
print(sorted(res))
