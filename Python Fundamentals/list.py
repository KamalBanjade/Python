numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[1])

# Mutable
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers)
numbers.append(100)  # to add at the end of the list
print(numbers)
numbers[0] = 11  # to modify the element of index 0
print(numbers)
numbers.remove(20)  # to remove the first occurence of 20
print(numbers)
numbers.pop(4)  # to remove the element of 4th index
print(numbers)

# Allow Duplicate
duplicates = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
print(duplicates)

print("\n")
# common list operations

# 1. Accessing elements
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[0])  # returns the element of first index
print(my_list[-1])  # returns the element of last index

# 2. Slicing
print(my_list[1:4])  # starting from 1 index, it returns values upto 3rd index but don't goto 4th even if there is 4
print(my_list[:3])  # starting from 0 index, it returns the values upto 2nd index
print(my_list[1:4:2])  # starting from 1 to ending at 4 returning the value upto 3rd index, it skips 2 steps

# 3. extend
my_list.extend([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(my_list)  # it extends the list by appending the entire adding list at once

my_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_lists.insert(3, 45)  # it inserts the value at any index, syntax: insert(index, inserting value)
print(my_lists)
my_lists.remove(4)
print(my_lists)

my_lists.clear()
print(my_lists)

# Checking Membership
my_listss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(3 in my_listss)
print(11 in my_listss)

# sort, reverse
print("Sort and reverse")
random = [9, 4, 5, 2, 8, 0, 3]
print(f"The random list is {random}")
random.sort()
print(f"The ascending sorted list is {random}")
random.sort(reverse=True)
print(f"The decending sorted  list is {random}")
randoms = [9, 4, 5, 2, 8, 0, 3]
randoms.reverse()
print(f"The reverse list is {randoms}")

# List Comprehensions
dynamic_list = [x ** 2 for x in range(5)]
print(f"The dynamic list is {dynamic_list}")
length = len(dynamic_list)
print(f"The length of dynamic list is {length}")
Count = dynamic_list.count(9)
print(f"The count of 9 in dynamic list is {Count}")
index = dynamic_list.index(4)
print(f"The index of 4 in dynamic list is {index}")
