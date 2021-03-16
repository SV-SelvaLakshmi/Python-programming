my_list= [1,2,3,4,5,7,9,11]
def odd_one(item):
  return item%2!=0

print(list(filter(odd_one,my_list)))
print(my_list)
