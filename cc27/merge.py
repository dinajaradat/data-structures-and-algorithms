def Mergesort(arr):
    n = len(arr)
    if n == 0 :
        return []
    if n > 1:
        mid = n //2
        left = arr[:mid]
        right = arr[mid:]
        
        left.sort()
        # print(left)
        right.sort()
        # print(right)

        return Merge(left, right, arr)

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    sorted = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

        k += 1
    
    while i < len(left):
        sorted.append(left[i])
        i += 1

    while j < len(right):
        sorted.append(right[j])
        j += 1

    return sorted



arr = [8,4,23,42,16,15]
print(Mergesort(arr))