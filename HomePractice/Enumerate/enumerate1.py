'''
The enumerate() function in Python is a built-in function that 
simplifies looping through an iterable while simultaneously accessing both 
the index and the value of each element. It returns an enumerate object, 
which produces pairs of (index, value) tuples during iteration.
Syntax:
  enumerate(iterable, start=0)
Parameters:
  iterable: Any iterable object (e.g., list, tuple, string, dictionary, 
            set) that you want to iterate over.
  start (optional): An integer specifying the starting index for the counter. 
                    By default, it is 0.
'''
fruits = ["apple", "banana", "cherry"]
# Using enumerate with default start index
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
print("---")
# Using enumerate with a custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"Item {index}: {fruit}")