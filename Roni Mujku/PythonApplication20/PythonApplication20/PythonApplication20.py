arr = [6,23,54,8,28,2,576,22,5,7]

print(arr)

def BubbleSort(arr):
    for i in range (len(arr)-1):

        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                print(arr)

def InsertSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0) & (arr[j] > key):
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

InsertSort(arr)

print(arr)