# covid-19
# number of case by city
cases = [50, 10, 100, -1, 0, 50, -1, 100, 100, 100]  #/ -1 no data

# alg1: calc total/sum of values
#s = cases[0] + cases[1] + cases[2] + cases[3] + cases[4]
#print("Total cases:", s)
s = 0
for c in cases:
    if c >= 0:
        s += c

print("Total cases:", s)   

