"""
[프로그래머스_해시_위장]
"""
def solution(clothes):
    answer = 1
    hashmap = {}
    for cloth in clothes:
        if not hashmap.get(cloth[1]):
            hashmap[cloth[1]] = 1
        else:
            hashmap[cloth[1]] +=1 
    print(hashmap)
    item_list = list(hashmap.values())
    for v in item_list:
        answer *= v +1
    answer -= 1
    return answer

""" # ㅋㅋ....쓰레기 내코드!

count = len(clothes)
print(count)
for i in range(len(clothes)):
    key = clothes[i][0]
    value = clothes[i][1]
    for j in range(i+1,len(clothes)):
        k = clothes[j][0]
        v = clothes[j][1]
        if v == value:
            continue
        else:
            print(v,value)
            count += 1
            
print(count)
"""
