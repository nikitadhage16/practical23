# a) Create a tuple
my_tuple = (10, 20, 30)
print("Original Tuple:", my_tuple)

# b) Access elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# c) Update tuple element
# Tuples are immutable, so we convert to list first
temp_list = list(my_tuple)
temp_list[1] = 25  # Change 2nd element
my_tuple = tuple(temp_list)
print("After updating 2nd element:", my_tuple)

# d) Delete element from tuple
temp_list = list(my_tuple)
del temp_list[0]  # Delete 1st element
my_tuple = tuple(temp_list)
print("After deleting 1st element:", my_tuple)

