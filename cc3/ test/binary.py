def Binary_Search(array,key):
  if len(array) <= 1:
        if len(array) == 1 and key == array[0]:
            return 0
        else:
            return -1
  mid = len(array) // 2

  if key == array[mid]:
       return mid
  elif key < array[mid]:
        return Binary_Search(array[0:mid],key)
  elif key > array[mid]:
      result = Binary_Search(array[mid+1:],key) 
      if result == -1:
            return -1
      else:
            return result + mid + 1
