array = [-5, 2, 3, 4, 5, 4, 7, 8, 9, 10, 7, -7]
subArray = []
numSubArray = int(input('Enter N: '))
sumSubArray = 0

for x in range(0, numSubArray):
    largeNum = 0
    for y in range(len(array)):
        if array[y] > largeNum:
            largeNum = array[y]
    array.remove(largeNum)
    subArray.append(largeNum)

print(subArray)

for i in range(0, len(subArray)):    
   sumSubArray = sumSubArray + subArray[i];    
     
print("Sum of all the elements of an array: " + str(sumSubArray));