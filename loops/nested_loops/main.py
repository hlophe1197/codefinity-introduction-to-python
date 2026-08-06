produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

#Combine the two lists 
groceries = [produce , dairy]
print(groceries)

#List of lists representing sections in the grocery store

for section in groceries:
    print(section)
    for item in section:
      print("Item name:", item)
 
 









