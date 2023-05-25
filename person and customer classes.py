#Brian Webb
#ITECH209
#4/22/2023


class Person:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, mailing_list):
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

#Commented out customer information
#customer1 = Customer("Brian Webb", "123 SIU St.", "123-4567", 12345, True)

#print(customer1.name)
#print(customer1.address)
#print(customer1.telephone)
#print(customer1.customer_number)
#print(customer1.mailing_list)
