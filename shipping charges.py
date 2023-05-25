weight_of_package = float(input("Enter weight of package: "))
shipping_charges = 0.0

message = "Shipping charges = "

if weight_of_package <= 2:
    shipping_charges = weight_of_package * 1.50
elif weight_of_package > 2 and weight_of_package <= 6:
    shipping_charges = weight_of_package * 3.00
elif weight_of_package > 6 and weight_of_package <= 10:
    shipping_charges = weight_of_package * 4.00
elif weight_of_package > 10:
    shipping_charges = weight_of_package * 4.75

message += "$" + format(shipping_charges, ',.2f')

print(message)
