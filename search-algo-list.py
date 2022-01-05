### SEARCH ALGO VARIATIONS:
# - ITERATE
# - COMPARE
# - COMPARE
# - REMEMBER

item      = "Irina"  # this is what we search for
container = ["John", "Marry", "Bob"] # where to look for
for i in range(len(container)):
    found     = container[i] == item  # remember
    # print(">>>", i, container[i] == item)
    if found:
        break
    

if found:                       # check the memory
    print(item, "Found")
else:
    print(item, "NOT Found")

