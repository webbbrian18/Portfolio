#Brian Webb
#3/6/23
#ITEC209
#I am sorry I uploaded the wrong file.
speed = float(input("Enter the speed of the vehicle in miles per hour: "))
hours = int(input("Enter the number of hours the vehicle has traveled: "))

print("Hour\tDistance Traveled")
print("------------------------------")
for hour in range(1, hours + 1):
    distance = speed * hour
    print(hour, "\t\t", distance)
