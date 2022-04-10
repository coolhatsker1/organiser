def bubbleSort(arr, a, b):
    for i in range(b - 1):
        for j in range(0, b - a - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selectionSort(arr, a, b):
    for a in range(b):
        min_idx = a
        for j in range(a + 1, b):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[a], arr[min_idx] = arr[min_idx], arr[a]


def insertionSort(arr, a, b):
    for i in range(a, b):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


a = 0
b = 0

int asss;

print("UnSorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

bubbleSort(arr, a, b)

print("BubbleSorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

selectionSort(arr, a, b)

print("SelectionSorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

insertionSort(arr, a, b)

print("InsertionSorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

print("Hello World")
