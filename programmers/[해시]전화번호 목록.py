"""
프로그래머스_해시_전화번호목록
"""
def solution(phone_book):
    answer = True
    phone_book.sort()
    for p1,p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            answer = False
            
            
"""
해시 구성,
- 요소 별로 temp 만들면서 temp 가 해시 키에 있는지
"""
#     hash_map = {}
#     for number in phone_book:
#         hash_map[number] = 1

#     for number in phone_book:
#         temp = ""
#         for n in number:
#             temp += n
#             if temp in hash_map and temp != number:
#                 answer = False
    return answer
