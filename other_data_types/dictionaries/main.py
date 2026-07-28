#Dictionary for a grocery store inventory
grocery_inventory = {"Milk":(113,"Dairy"), "Eggs":(116,"Dairy"), "Bread":(117,"Bakery"),"Apples":(141,"Produce")}

#Retrieving the details of bread
bread_details = grocery_inventory.get("Bread")
print("Details of Bread:", bread_details)

#Updating grocery inventory by adding a new item
grocery_inventory.update({"Cookies":(143, "Bakery")})
print("Inventory after adding Cookies:", grocery_inventory)

#Remove eggs from the grocery inventory
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)


