import math
def solution(progresses, speeds):
    answer = []
    time_lst = []
    count = 1
    front = 0
    
    for i in range(len(progresses)):
        a = progresses[i] 
        b = speeds[i]
        tmp_time = math.ceil((100-a) / b)
        time_lst.append(tmp_time)

    for idx in range(len(time_lst)):
        if time_lst[idx] > time_lst[front]:  
            answer.append(idx - front)
            front = idx 
    answer.append(len(time_lst) - front)         
    return answer
