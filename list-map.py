# 0 - free
# 1 - unavailable

parking = [0, 0, 0, 0, 1, 1, 0]

# user input
index_to_park = int(input("Where? "))

if index_to_park in range(0, len(parking)):
    if parking[index_to_park] == 1:
        print("Unavailable!")
    else:
        print("You can park there!")    
        parking[index_to_park] = 1
else: 
    print("Index out of range!")


for index in range(0, len(parking)):
    if parking[index] == 1:
        print(index, "[ x ]")
    elif parking[index] == 0:
        print(index, "[   ]")
