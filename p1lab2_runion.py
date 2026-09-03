# CTI 110
# P1LAB2 - Selling Things
# Runiona
# 9/3/26

# Fictional Store -- pick three things 
# product_name, product_count, product_price

#change these to own values
product_name = "CPU"
product_count = 400
product_price = 239.99

print("STORE STARTUP")
print("_" * 10)
product_name = input("Enter product name: ")
product_count = input("Enter product count: ")
product_price = input("Enter product price: ")

product_count = int(product_count)
product_price =float(product_price)
total = product_count * product_price

print("CUSTOMER INTERFACE")
print("_" * 10)
print("Welcome to the", product_name, "store")
print(f"we have {product_count} {product_name}(s) at ${product_price:.2f} each.")
print(f"Total is: ${total:.2f}.")

total = product_count * product_price


