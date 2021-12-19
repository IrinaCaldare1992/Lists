
matrix = [
    [1, 2, 0],
    [4, 5, 6],
    [2, 8, 9]

]

### sum of main diagonal values ###
# smd = matrix[0][0] + matrix[1] [1] + matrix[2][2]

smd = 0
for di in range(3):
    smd = smd + matrix[di][di]

print("Sum of main diagonal is: ", smd)

### sum of main diagonal values ###

### sum of secondary diagonal values ###

ssd = 0
for sdi in range(3):
    ssd = ssd + matrix[sdi][3-sdi-1]

print("Sum of secondary diagonal is: ", ssd)

### sum of secondary diagonal values ###

####### 2nd walk #######

for ri in range(3):
    row = matrix[ri]

    for ci in range(3):
        column = row[ci]
        print(ri, ci, ">", column)

####### 2nd walk #######


