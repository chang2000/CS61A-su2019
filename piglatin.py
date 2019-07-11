def piglation(word):
    flag = -1
    for i in range(len(word)):
        if i == 'a' or 'i' or 'e' or 'o' or 'u':
            flag = i
    if flag == -1:
        return word+"ay"
    if flag ==



