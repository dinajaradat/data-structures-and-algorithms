def insert(sorted_list, value):
    i = 0
    while value > sorted_list[i]:
        i += 1
    while i < len(sorted_list):
        temp = sorted_list[i]
        sorted_list[i] = value
        value = temp
        i += 1
    sorted_list.append(value)


def InsertionSort(input_list):
    len_input = len(input_list)
    sorted_list = []
    if len_input == 0:
        return []
    sorted_list.append(input_list[0])

    for i in range(1, len_input):
        insert(sorted_list, input_list[i])

    return sorted_list




if __name__ == "__main__":
    input = [58,18,-1,8,5,-2,-10]
    sorted = InsertionSort(input)
    print(sorted)