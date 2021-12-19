guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]

total_guests = guests_1 + guests_2 + guests_3
final_list = []
for i in total_guests:
    if i not in final_list:
        final_list.append(i)
final_list.sort()
print(final_list)
