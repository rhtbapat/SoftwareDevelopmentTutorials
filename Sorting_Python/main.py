import sys
sys.setrecursionlimit(100000000) #Very Very Important!!!!!!

import random
import datetime
from SelectionSort import *
from InsertionSort import *
from BubbleSort import *
from QuickSort import *
from MergeSort import *
from HeapSort import *
from ReverseArray import *
from ShellSort import *

def printArray(arr1):
  for arr in arr1:
    print('{0:2s} {1:3s} {2:4s} {3:5s}'.format(arr[0], arr[1], arr[2], arr[3]))

arr1 = []
arr2 = []
arr3 = []

arr4 = []
arr5 = []
arr6 = []

arr7 = []
arr8 = []
arr9 = []

arr10 = []
arr11 = []
arr12 = []

arr13 = []
arr14 = []
arr15 = []

arr16 = []
arr17 = []
arr18 = []

arr19 = []
arr20 = []
arr21 = []

strArr = "abcdef ghij @#%$%$ sfrgdr"
numArray = []

tempVal = 0
N = 8500
i = 0

for i in range(0,N):
  tempVal = random.randrange(1,10*N)
  arr1.append(tempVal)
  arr2.append(i)
  arr3.append(10*N - i)
  
  arr4.append(tempVal)
  arr5.append(i)
  arr6.append(10*N - i)
  
  arr7.append(tempVal)
  arr8.append(i)
  arr9.append(10*N - i)
  
  arr10.append(tempVal)
  arr11.append(i)
  arr12.append(10*N - i)
  
  arr13.append(tempVal)
  arr14.append(i)
  arr15.append(10*N - i)
  
  arr16.append(tempVal)
  arr17.append(i)
  arr18.append(10*N - i)

  arr19.append(tempVal)
  arr20.append(i)
  arr21.append(10*N - i)
  
  numArray.append(tempVal)

sortingTimeTableArray = [["Sorting Algorithm", "Random        ", "Best          ", "Worst"]]

# Selection sorted
print("Selection sorted - Random  Best Case  Worst Case")
selectionSortTimings = ["Selection Sort   "]
start = datetime.datetime.now()
arr1 = SelectionSort(arr1)
selectionSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr2 = SelectionSort(arr2)
selectionSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr3 = SelectionSort(arr3)
selectionSortTimings.append(str(datetime.datetime.now() - start))
sortingTimeTableArray.append(selectionSortTimings)

# Insertion sorted
print("Insertion sorted - Random  Best Case  Worst Case")
insertionSortTimings = ["Insertion Sort   "]
start = datetime.datetime.now()
arr4 = InsertionSort(arr4)
insertionSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr5 = InsertionSort(arr5)
insertionSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr6 = InsertionSort(arr6)
insertionSortTimings.append(str(datetime.datetime.now() - start))
sortingTimeTableArray.append(insertionSortTimings)

# Bubble sorted
print("Bubble sorted - Random  Best Case  Worst Case")
bubbleSortTimings = ["Bubble Sort      "]
start = datetime.datetime.now()
arr7 = BubbleSort(arr7)
bubbleSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr8 = BubbleSort(arr8)
bubbleSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr9 = BubbleSort(arr9)
bubbleSortTimings.append(str(datetime.datetime.now() - start))
sortingTimeTableArray.append(bubbleSortTimings)

# QuickSort sorted
print("Quick sorted - Random  Best Case  Worst Case")
quickSortTimings = ["Quick Sort       "]
start = datetime.datetime.now()
arr10 = QuickSort(arr10,0,N-1)
quickSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr11 = QuickSort(arr11,0,N-1)
quickSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr12 = QuickSort(arr12,0,N-1)
quickSortTimings.append(str(datetime.datetime.now() - start))
sortingTimeTableArray.append(quickSortTimings)

# Merge sorted
print("Merge sorted - Random  Best Case  Worst Case")
mergeSortTimings = ["Merge Sort       "]
start = datetime.datetime.now()
arr13 = MergeSort(arr13)
mergeSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr14 = MergeSort(arr14)
mergeSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr15 = MergeSort(arr15)
mergeSortTimings.append(str(datetime.datetime.now() - start))
sortingTimeTableArray.append(mergeSortTimings)

# Heap sorted
print("Heap sorted - Random  Best Case  Worst Case")
heapSortTimings = ["Heap Sort        "]
start = datetime.datetime.now()
arr16 = HeapSort(arr16)
heapSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr17 = HeapSort(arr17)
heapSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr18 = HeapSort(arr18)
heapSortTimings.append(str(datetime.datetime.now() - start))
sortingTimeTableArray.append(heapSortTimings)

# Shell sorted
print("Shell sorted - Random  Best Case  Worst Case")
shellSortTimings = ["Shell Sort       "]
start = datetime.datetime.now()
arr19 = ShellSort(arr19)
shellSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr20 = ShellSort(arr20)
shellSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
arr21 = ShellSort(arr21)
shellSortTimings.append(str(datetime.datetime.now() - start))
start = datetime.datetime.now()
sortingTimeTableArray.append(shellSortTimings)

printArray(sortingTimeTableArray)

# Reverse Oder
print("Reverse String Array")
print(strArr)
strArr = ReverseStringArray(strArr)
print(strArr)
print("Reverse Number Array")
print(numArray)
numArray = ReverseNumArray(numArray)
print(numArray)