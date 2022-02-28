from collections import Counter

def solution(participant, completion):
    counter = Counter(participant)
    counter2 = Counter(completion)
    key = participant
    answer = ''
    for i in range(len(counter)):
        if counter[key[i]] != counter2[key[i]]:
            answer = key[i]
            break
    return answer
