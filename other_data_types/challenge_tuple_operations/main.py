# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#Counting the number of times apples appear in the shelf tuple
apple_count = shelf.count("apples")
print("Number of apples:", apple_count)

#Finding the index of the first occurence of bananas
banana_index = shelf.index("bananas")
print("First banana index:", banana_index)

#Checking if the number of apples is less than 5
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

#Count how many times grapes appear in the shelf tuple
grapes_count = shelf.count("grapes")

if grapes_count <= 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

#Checking if oranges exist in shelf tuple
orange_index = shelf.index("oranges")

if "oranges" in shelf:
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")




