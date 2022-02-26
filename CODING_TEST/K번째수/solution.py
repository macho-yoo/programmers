def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        tmp_array = array[commands[i][0] -1  :commands[i][1]   ]
        tmp_array.sort()
        answer.append(tmp_array[commands[i][2] -1])
    return answer
