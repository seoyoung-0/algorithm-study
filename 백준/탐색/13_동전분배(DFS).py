# 동전분배하기-dfs
# 최대,최소 차가 가장 적도록 3명에게 동전 분배
# n = 7, num = [8,9,11,12,23,15,17]

money = [0] * 3

def dfs(index):
    global res
    
    if index == n:
        m_sub = max(money) - min(money)
        if m_sub < res:
            tmp = set()
            for x in money:
                tmp.add(x) # 중복아닐 때
            if len(tmp) == 3:
                print(money)
                res = m_sub
                
    else:
        # 3 명에게 분배
        for i in range(3):
            money[i] += num[index]
            dfs(index+1) # 다음 동전
            money[i] -= num[index]

n = int(input())
res = 214700000
num = []
for i in range(n):
    num.append(int(input()))
dfs(0)
print('res',res)
