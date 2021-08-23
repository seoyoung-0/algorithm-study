# 1629
# a를 b 번 곱한 수 , 매우 커질 수 있으므로 이를 c 로 나눈 나머지를 구하기
'''
2^10 -> 2^5 * 2^5
2^11 -> 2^5 * 2^5*2 : 홀수라면 a
b 를 절반으로 나눠서 계산..O(logb)
'''

def recursive_01(a,b,c):
    if b == 1:
        return a % c
    val = recursive_01(a,b//2,c)
    
    if b % 2 == 0:
        return val * val % c
    else:
        return val * val * a % c

a,b,c = map(int, input().split())

print(recursive_01(a,b,c))
