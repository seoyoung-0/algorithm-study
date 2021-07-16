# https://leetcode.com/problems/reorder-data-in-log-files/
'''
937_로그파일 재정렬

-> lambda 다중 조건으로 sort
'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        for log in logs:
            words = log.split(' ')
            if words[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

                
        # letters.sort(key = lambda x:(x.split()[1:],x.split()[0])) 
        # 쪼개고 바로 key로 사용 -> 다시 문장으로 안 만들어줘도 된다.

        
        let = []
        for i in range(len(letters)):
            let.append(letters[i].split(' '))
            let.sort(key = lambda x:(x[1:],x[0]))    

        fin = []
        for l in let:
            res =' '.join(l)
            fin.append(res)

        return fin + digits
