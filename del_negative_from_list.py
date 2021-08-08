# initializing list
test_list =list(map(int, input().split(",")))
  
# printing original list
print("The original list is : " + str(test_list))
  
# Remove Negative Elements in List
# Using list comprehension
res = [ele for ele in test_list if ele > 0]
  
# printing result 
print("List after filtering : " + str(res))
