#Creation of grocery inventory dictionary
grocery_inventory = {"Milk":("Dairy",3.50,8),"Eggs":("Dairy",5.50,30),"Bread":("Bakery",2.99,15),"Apples":("Produce",1.50,50)}
print(grocery_inventory)

#Checking if Eggs price exceeds $5
Eggs_price = grocery_inventory["Eggs"][1]
print("Price of eggs:", Eggs_price)

category, price, stock = grocery_inventory["Eggs"]
if Eggs_price > 5:
    #Rebuild the tuple with reduced price
    grocery_inventory["Eggs"] = (category, price -1, stock)
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of eggs is reasonable.")

#Adding new item called Tomatoes
grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

#Storing Milk into milk stock
milk_stock = grocery_inventory["Milk"][2]
print("Milk stock:", milk_stock)

category, price, stock = grocery_inventory["Milk"]
if milk_stock < 10:
    #Rebuild the tuple with increased stock
    grocery_inventory["Milk"] = (category, price, stock +20)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

apples_price = grocery_inventory["Apples"][1]
print("Price of apples:", apples_price)

category, price, stock = grocery_inventory["Apples"]
if apples_price > 2:
    #Rebuild the tuple by removing the item called Apples
    grocery_inventory.remove("Apples")
    print("Apples removed from inventory due to high price.")

#Printing updated inventory
print("Updated inventory:", grocery_inventory)
    








