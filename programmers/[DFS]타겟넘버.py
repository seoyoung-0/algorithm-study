'''
numbers = [1,1,1,1,1], target = 3 ,answer = 5
'''
answer = 0

def solution(numbers, target):
    
    sub = 0 
    
    def dfs(index,sub):
        
        if (index == len(numbers) and sub == target):
            
            #nonlocal answer
            
            global answer
    '''

    answer 값이 변경이 안되는 error 발생
    (1) solution 안에 answer 있으면, dfs 에서는 nonlocal answer 하고 answer 조작
    
    (2) 아예 solution 밖에 answer 선언하면, 전역 변수 사용하겠다고
    global answer 해주고 조작 (solution, dfs 에서)
    
    '''
            answer += 1
            return 
    
        if index == len(numbers):
            return 

        dfs(index+1, sub + numbers[index])
        dfs(index+1, sub - numbers[index])
        
        
    dfs(0,sub)
    global answer
    
    return answer
