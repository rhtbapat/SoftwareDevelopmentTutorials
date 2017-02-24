def ReverseStringArray(arr):
  left = 0
  right = len(arr)-1
  arr = list(arr)
  while(left < right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left = left + 1
    right = right - 1
  return ''.join(arr)
  
def ReverseNumArray(arr):
  left = 0
  right = len(arr)-1
  while(left < right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left = left + 1 
    right = right - 1 
  return arr