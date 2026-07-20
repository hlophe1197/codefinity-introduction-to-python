# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120 

#Check if "raw" and "Imported" are in description
contains_raw = "raw" in description
contains_Imported = "Imported" in description

#Print the presence of these keywords to decide on the likelihood of the product being a success 

print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)

#Checking if the data typed are as expected
price_is_float = type(price) == float
count_is_int = type(count) == int

#Print the results to verify data types
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)












