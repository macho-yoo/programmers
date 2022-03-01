def solution(answers):
    answer = []

    lst1 = [1,2,3,4,5]
    count1=0
    lst2 = [2,1,2,3,2,4,2,5]
    count2 = 0
    lst3 = [3,3,1,1,2,2,4,4,5,5]
    count3 = 0

    for i in range(len(answers)):

        if lst1[i%5] == answers[i]:
            count1 += 1
        if lst2[i%8] == answers[i]:
            count2 += 1
        if lst3[i%10] == answers[i]:
            count3 += 1
    score_lst = [count1,count2,count3] 

    for i in range(3):
        if score_lst[i] == max(score_lst):
            answer.append(i+1)
    return answer
