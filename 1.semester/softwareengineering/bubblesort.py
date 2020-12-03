def bubbleSort(list):
    for elements in range(len(list)-1,0,-1):
        for i in range(elements):
            if list[i]<list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return(list)

list = [19, 96, 33, 7, 27, 31, 45, 21, 79, 82, 63]
bubbleSort(list)
print(list)

