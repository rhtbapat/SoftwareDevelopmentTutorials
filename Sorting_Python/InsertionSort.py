def InsertionSort(arr):
	i = 0
	j = 0
	tempVal = 0
	for i in range(0,len(arr)):
		j = i 
		while(j > 0 and arr[j] < arr[j-1]):
			tempVal = arr[j]
			arr[j] = arr[j-1]
			arr[j-1] =  tempVal
			j = j - 1
		i = i + 1
	return arr