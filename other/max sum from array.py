#problem: find the max sum from the given sub array 
# but it can't remove the repeated numbers from the array.


array = [-5, 2, 3, 4, 5, 4, 7, 8, 9, 10, 7, -7, -10, 10] #input array
subArray = [] #sub array is defined
elementsSubArray = int(input('Enter N: ')) #number of items from the array to be used in the sub array
sumSubArray = 0 #sum of the sub array

for x in range(0, elementsSubArray): #loop to get the items from the array
    largeNum = 0 #largest number in the sub array
    for y in range(len(array)): #loop to get the largest number in the sub array
        if array[y] > largeNum: #if the number is larger than the largest number in the sub array
            largeNum = array[y] #set the largest number in the sub array to the number
    array.remove(largeNum) #remove the largest number from the array
    subArray.append(largeNum) #add the largest number to the sub array

print(subArray) #print the sub array

for i in range(0, len(subArray)): #loop to get the sum of the sub array  
   sumSubArray = sumSubArray + subArray[i]; #sum of the sub array  
     
print("Sum of all the elements of an array: " + str(sumSubArray)); #print the sum of the sub array