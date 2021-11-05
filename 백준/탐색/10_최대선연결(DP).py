# 4. 최대 선 연결하기 (LIS응용)
# 1~10 나열과 연결했을 때 선 겹치지 않고 최대 몇 개 연결 가능

N = int(input())
arr = list(map(int, input().split())) #오른쪽 줄 
arr.insert(0,0)
save = [0] * (N+1)

# arr = 0,4 1 2 3 9 7 5 6 10 8 
for i in range(1, N+1):
    pre_max = 0
    for j in range(i-1,0,-1):
        if arr[j] < arr[i]:
            pre_max = max(pre_max, save[j])
    save[i] = pre_max + 1

print(save)
print(max(save))
