# 5 star rating for users / int
rating = [5, 3, 1, 4, 5, 2, 5]

# alg1: inter + print + index
print("username / rating")
for i in range(len(rating)):
    print ("user", i+1, " = ", rating[i], end = " ")
    for r in range(rating[i]):
        print("*", end = "")
    print()