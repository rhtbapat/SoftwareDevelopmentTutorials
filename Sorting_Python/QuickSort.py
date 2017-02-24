def partition(arr, start, end):
    pivot = arr[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=arr[left]
            arr[left]=arr[right]
            arr[right]=temp
    # swap start with arr[right]
    temp=arr[start]
    arr[start]=arr[right]
    arr[right]=temp
    return right
	
def QuickSort(arr, start, end):
    if start < end:
        # partition the list
        pivot = partition(arr, start, end)
        # sort both halves
        QuickSort(arr, start, pivot-1)
        QuickSort(arr, pivot+1, end)
    return arr