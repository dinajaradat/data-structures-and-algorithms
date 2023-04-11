def insertSheftArray(array, value):
  new_Array = []
  if len(array) == 0:
    new_Array.append(value)
    return new_Array

  mid = len(array) // 2

  for i in range(len(array)):
    if i == mid:
      new_Array.append(value)
      new_Array.append(array[i])
    else:
      new_Array.append(array[i])
  return new_Array

def remove_middle_element(array):
  mid = len(array) // 2
  array.pop(mid)
  return array
