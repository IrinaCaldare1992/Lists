p = ["Mercedes", None, "BMW", None, None, "Toyota", "BMW"]
# index  0,    1,    2,    3,    4,       5,     6

user_car_brand = input("Name your brand:?")
user_park_index = int(input("What place:?"))
if p[user_park_index] == None:
    print("Okay, You can park there")
    p[user_park_index] = user_car_brand
else:
    print("This place is not available!!!")

# FREE/TOTAL PARKING LOTS
total = len( p )
free = 0
for i in range(len(p)):
    if p[i] == None:
        free += 1    
print("Free/Total parking lots: ", free, "/", total, "places")


for i in range(len(p)):
    print(i, p[i])

Mercedes = p.count("Mercedes")
BMW = p.count("BMW")
Toyota = p.count("Toyota")

print("Mercedes: ", Mercedes, "BMW: ", BMW, "Toyota: ", Toyota)
