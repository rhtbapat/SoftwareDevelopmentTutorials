def ShellSort(arr):
  sublistcount = len(arr)//2
  while sublistcount > 0:

    for startposition in range(sublistcount):
      SortWithGap(arr,startposition,sublistcount)

    sublistcount = sublistcount // 2
  return arr
  
  
def SortWithGap(arr,start,gap):
    for i in range(start+gap,len(arr),gap):

        currentvalue = arr[i]
        position = i

        while position>=gap and arr[position-gap]>currentvalue:
            arr[position]=arr[position-gap]
            position = position-gap

        arr[position]=currentvalue