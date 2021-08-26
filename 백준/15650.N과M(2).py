# 15650
# 중복없이 nCm

def func(sub, remain):
    if len(sub) == m:
        res.append(sub[:])
        return
    else:
        for i,n in enumerate(remain):
            
            prev = remain[i:] ###자기보다 작은 수는 remain에 사용x
            sub.append(n)
            prev.remove(n)
            func(sub,prev)
            sub.pop()
            
n,m = map(int, input().split())
res = []
sub = []
remain = [i+1 for i in range(n)]
func(sub, remain)
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j], end=' ')
    print()
