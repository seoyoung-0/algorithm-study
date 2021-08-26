# nPm

def func(sub, remain):
    if len(sub) == m:
        res.append(sub[:])
        return 
    else:
        for n in remain:
            prev = remain[:]
            sub.append(n)
            prev.remove(n)
            func(sub,prev)
            sub.pop()
            
n, m =  map(int, input().split())
res = []
sub = []
remain = [i+1 for i in range(n)]
func(sub,remain)

for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j], end=' ')
    print()
    

''' 내 풀이
def func(sub, remain):
    print(sub, remain)
    
    for i in range(0,N):
        sub.append(remain.pop(i))
        
        while remain:
            sub.append(remain.pop(0))
            print(sub)
            if len(sub) == M:
                for n in sub:
                    print(n, end =' ')
                print()
            sub.pop()
        sub.pop() 

        remain = [i+1 for i in range(N)]
'''
