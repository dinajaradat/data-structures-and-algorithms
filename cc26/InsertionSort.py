def insert (sorted , value):
    i = 0
    while value > len(sorted):
        i+=1
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value 
        value = temp
        i+=1
    sorted.append(value)

def InsertionSort(input):
    sorted = []
    sorted.append(input[0])

    for i in range (1, len(input)):
        insert(sorted , input[i])
    return sorted


if __name__ == "__main__":
    input = [20,18,12,8,5,-2]
    sorted = InsertionSort(input)
    print(sorted)