# 1182 
# 원하는 합 만드는 부분집합 개수 
## 공집합 제외

def subset(index, path):
    print(path)
    if sum(path) == s and path:
        global cnt
        cnt += 1
    
    for i in range(index, len(num)):
        subset(i+1, path + [num[i]])

n, s = map(int, input().split())
number = str(input())
num = list(map(int, number.split(' ')))
cnt = 0

subset(0,[])
print(cnt)
