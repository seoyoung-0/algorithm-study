def solution(numbers):
    answer = 0
    res = []
    
    def dfs(sub, remain): # 만들수있는 모든 숫자
        if sub:
            number = int(''.join(map(str, sub)))
            if number not in res:
                res.append(number)
                
        for n in remain:
            sub.append(n)
            prev = remain[:]
            prev.remove(n)
            dfs(sub, prev)
            sub.pop()
    
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    
    num = list(map(int, str(numbers)))
    dfs([], num)
    
    for r in res:
        if isPrime(r):
            answer += 1
            
    return answer
