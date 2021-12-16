# 알파코드(DFS)

# graph = {}
# for i in range(65,91):
#     graph['i-64'] = chr(i)
    
def dfs(L,p):
    if L == n:
        global cnt
        cnt += 1
        sub = []
        for r in range(p):
            sub.append(chr(res[r]+64)) ###그래프 필요없음;;
        print(' '.join(sub))
    
    else:
        for i in range(1,27): #1~26 전체를 매번 돌기..
            if code[L]==i:
                res[p] = i
                dfs(L+1,p+1)
            elif i>=10 and code[L]==(i//10) and code[L+1]==(i%10):
                res[p] = i
                dfs(L+2, p+1)
                
code = list(map(int, input()))
n = len(code)
code.insert(n,-1) #L+1 방지
res = [0] * (n+3)
cnt = 0
dfs(0,0)
print(cnt)
