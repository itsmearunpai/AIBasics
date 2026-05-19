#List
my_list = ["Apple", "Banana", "Cherry"
]
print(my_list)

my_numbers = [1, 2, 3, 4, 5]
print(my_numbers)

print("Extract list items",my_list[0:-1])

print("Exclude first and last item",my_list[1:-1])
my_list.append("Date")
print("After appending Date",my_list)

if "Banana" in my_list:
    print("Banana is in the list")

    #List comprehension

squared_numbers = [x**2 for x in my_numbers]
print("Squared numbers:", squared_numbers)

#Example of sets
my_set = {1, 2, 3, 4, 5}
print("My set:", my_set)

#Tuples
my_tuple = ("Red", "Green", "Blue")
print("My tuple:", my_tuple)

