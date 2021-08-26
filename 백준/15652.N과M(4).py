# 15652

def func(sub, remain):
    if len(sub) == m:
        print(' '.join(map(str, sub))) 
        
    else:
        for i,n in enumerate(remain):
            prev = remain[i:]
            sub.append(n)
            func(sub,prev)
            # n을 prev 에서 제거하지 않고, 
            # 수 조합 만든 후에 리턴받은 후 제거 
            prev.remove(n)
            sub.pop()
            
n,m = map(int, input().split())
res = []
sub = []
remain = [i+1 for i in range(n)]
func(sub, remain)
