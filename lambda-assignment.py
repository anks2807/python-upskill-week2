from functools import reduce

# double the array elements using lambda function and map
a = [1,2,3,4]
print(list(map(lambda x: x*2, a)))

#filter even numbers from the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x%2 == 0, numbers)))

#longest word from the list using reduce and lambda
words = ["apple", "banana", "cherry", "date"]
print(reduce(lambda s1, s2: s1 if len(s1) > len(s2) else s2, words))

# square the float numbers and round to 1 decimal place using map and lambda
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
output = list(map(lambda x: round(x, 1), (list(map(lambda x: x**2, my_floats)))))
print(output)

# filter names with length less than or equal to 7 using filter and lambda
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
print(list(filter(lambda x: len(x) <= 7, my_names)))

# sum of all numbers in the list using reduce and lambda
numbers  = [1,2,3,4,5]
print(reduce(lambda x, y: x+y, numbers))