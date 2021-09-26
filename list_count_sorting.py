# print list based on it's count

ini_list = [1,5,1,2,2,1,4,5,1,3,3,5,1,2,4]

from collections import Counter

 
# printing initial ini_list
print ("initial list", str(ini_list))
 
# sorting on bais of frequency of elements
result = [i for i, c in Counter(ini_list).most_common()
                                      for i in [i] * c]
 
# printing final result
print("final list", str(result))

# # Python3 code to demonstrate
# # sorting and removal of duplicates
# # Using Counter.most_common() + list comprehension
# from collections import Counter
  
# # initializing list
# test_list = [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]
  
# # printing original list
# print("The original list : " + str(test_list))
  
# # using Counter.most_common() + list comprehension
# # sorting and removal of duplicates
# res = [key for key, value in Counter(test_list).most_common()]
  
# # print result
# print("The list after sorting and removal : " + str(res))