def insertionSort(array):

  for step in range (1, len(array)):
    key = array[step]
    j = step - 1


    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j = j - 1

        array[j + 1] = key


data = [99, 97, 93, 87, 81, 77, 73, 65, 63, 59, 55, 49, 47, 43, 39, 33, 31, 29, 25, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
insertionSort(data)
print('Array em ordem crescente: ')
print(data)
