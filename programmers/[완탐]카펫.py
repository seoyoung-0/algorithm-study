def solution(brown, yellow):
    answer = []
    blocks = brown + yellow
    
    def divide(total):
        num_list = []
        for i in range(1,total+1):
            if total % i == 0:
                if i >= total//i:
                    num_list.append((i,total//i))
        return num_list
    
    block_list = divide(blocks)
    yellow_list = divide(yellow)
    
    for b in block_list:
        for y in yellow_list:
            if (b[0]-y[0]) == (b[1]-y[1]):
                answer.append(b[0])
                answer.append(b[1])

    return answer
