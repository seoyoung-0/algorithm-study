# 15651

def func(sub, remain):
    if len(sub) == m:
        print(' '.join(map(str, sub))) ##시간초과 -> 별도 저장않고 바로 출력
        
    else:
        for n in remain:
            sub.append(n)
            func(sub,remain)
            sub.pop()
            
n,m = map(int, input().split())
res = []
sub = []
remain = [i+1 for i in range(n)]
func(sub, remain)
