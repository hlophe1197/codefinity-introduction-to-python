# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": [1.20, 50],   # "Item": [price, quantity sold]
    "Banana": [0.50, 100],
    "Cherry": [2.50, 25],
    "Mango": [1.75, 40]
}

total_sales_list = []

#Iterating through the products dictionary
for product, values in products.items():
    price = values[0]
    quantity = values[1]
    sales = price * quantity
    print(f"Total sales for {product}:${sales}")
    
    total_sales_list.append(sales)
    sum(total_sales_list)
    print(total_sales_list)
    

#Using built-in functions to find the total, maximum and minimum sales
total_sum = sum(total_sales_list)
print(f"Total sum of all sales: ${total_sum}")    
min_sales = min(total_sales_list)
print(f"Minimum sales: ${min_sales}")
max_sales = max(total_sales_list)
print(f"Maximum sales: ${max_sales}")

    



    

    


