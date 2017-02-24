def BubbleSort(arr):
  temp = 0
  needSorting = True
  i = 0
  while(needSorting):
    needSorting = False
    for i in range(0,len(arr)-1):
      if(arr[i+1] < arr[i]):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        needSorting = True
  return arr