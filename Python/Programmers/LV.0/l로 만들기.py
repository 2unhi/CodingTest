def solution(myString):
    answer = ''
    for alphabet in myString:
        if (alphabet < 'l'): answer += 'l'
        else: answer += alphabet
    return answer