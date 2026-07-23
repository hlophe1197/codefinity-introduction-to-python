#Create Lists
meat = ["Ham",3.99,50,"Sliced"]
cheese = ["Cheddar",5.49,100,"Sharp"]
condiment = ["Mustard",1.99,75,"Spicy"] 

#Create Nested List 
deli_dept = [meat,cheese,condiment]

#Print Nested List
print("Initial Deli List:",deli_dept)

#Updating meat list
meat[2] = 100

#Print Updated meat list
print(meat)

#Creating New Type Of meat List 
seasonal_meat = ["Turkey",4.50,100,"Sliced"]

#Print New Type Of meat list
print("seasonal meat:", seasonal_meat)


#Add New Type of meat List to deli_dept
deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)

#Sort deli_dept
deli_dept.sort(key=lambda item: item[0])

#Print Updated Deli list
print("Updated Deli List:",deli_dept)



