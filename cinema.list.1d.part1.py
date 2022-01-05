from os import system

# 0 - free
# 1 - reserved
# 2 - bought


seats = [0, 0, 1, 2, 0, 0, 0, 0]

option = -1

while option != 0:
    # iterative count algorithm
    free_seats = len(seats)

    for pi in range(len(seats)):
        if seats[pi] == 1:
            free_seats -= 1
        elif seats[pi] == 2:
            free_seats -= 1


    ######### PLOT #########
    system("cls")
    print()
    for pi in range(len(seats)):
        print("", pi+1, "", end = "  ")
    print()

    for pi in range(len(seats)):
        if seats[pi] == 1:
            print("/-/", end = "  ")
        elif seats[pi] == 2:
            print("/+/", end = "  ")
        else:
            print("/ /", end = "  ")
    print("\nFree seats: ", free_seats)
    print("\n")
    ######### PLOT #########


    # SHOW MENU ########

    print("MENU")
    print("1. Book")
    print("2. Buy")
    print("3. Cancel")
    print("0. Exit")
    print("-----------------------")

    # SHOW MENU ########

    # OPTION ###########

    option = int(input("Choose: "))

    if option == 1:
        place = int(input("Which seat: "))
        if place in range(len(seats)):
            seats[place -1] = 1
        else:
            print("Seat out of range or unavailable!")
    
    if option == 2:
        place = int(input("Which seat: "))
        if place in range(len(seats)):
            seats[place -1] = 2
        else:
            print("Seat out of range or unavailable!")
    if option == 3:
        place = int(input("Which seat: "))
        if seats[place-1] == 2:
            print("Action denied!")
        elif seats[place-1] == 0:
            print("Seat has not been booked!")
        else:
            seats[place -1] = 0
        