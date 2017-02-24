def SelectionSort(arr):
  tempId = 0;
  i = 0
  j = 0
  for i in range(0,len(arr)):
    tempVal = arr[i]
    tempId = i
    for j in range (i+1,len(arr)):
      if(arr[j] < tempVal):
        tempVal = arr[j]
        tempId = j
    temp = arr[i]
    arr[i] = arr[tempId]
    arr[tempId] = temp
  return arr