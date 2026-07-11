# Lists of items and categories for slicing
items = "bubblegum, chocolate, pasta"
categories = "candy aisle, pasta aisle"

candy1 = items[0:9]
candy2 = items[10:20]
dry_goods = items[21:]

print(candy1)
print(candy2)
print(dry_goods)

category1 = categories[0:11]
print(category1)

category2 = categories[12:]
print(category2)

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print(bubblegum_price)
print(chocolate_price)
print(pasta_price)

message = f"we have {candy1} for {bubblegum_price} in the {category1}"
print(message)

message = F"we have {candy2} for {chocolate_price} in the {category1}"
print(message)

message = F"we have {dry_goods} for {pasta_price} in the {category2}"
print(message)

