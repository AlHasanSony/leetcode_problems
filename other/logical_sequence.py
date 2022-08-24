


# x, y = map(int, input().split())
# count = 0

# while count < (y//x):
#     start = count*x + 1
#     end = (count + 1) * x + 1
#     for i in range(start,end,1):
#         print(i,end=" ")
#     print("")
#     count+=1


def print_lines(x, y):
   nums = list(range(y))
   for i in nums[::x]:
      print(" ".join([str(num + 1) for num in nums[i:i + x]]))

print_lines(3, 99)