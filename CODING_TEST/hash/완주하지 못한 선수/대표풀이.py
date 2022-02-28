import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

다른사람 풀이인데 어렵게 생각하지 않아도 Counter 객체는 뺄 수 있다는 것만 알아도 한줄풀이가 가능한 문제였다.
return에 문자열 answer 라고 적혀있다고 너무 맞추려 하지말고 내풀이에 return 값은 맞추면 깔끔하게 풀 수 있을것 
