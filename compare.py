# Compare Two CSV Files
file_list = ['Sample1.csv', 'Sample2.csv']

f1 = open(file_list[0], 'r').readlines()
f2 = open(file_list[1], 'r').readlines()

fName = open('Diffrence.csv', 'a')
for _ in range(2):
    for row in f1:
        if row not in f2:
            fName.write(row)
    f1, f2 = f2, f1


#HOW TO CREATE A PULL REQUEST
#STEP 1: CREATE A NEW BRANCH
#STEP2: Make your changes
#STEP3: Push it back to your repo
#STEP 4: Click the Compare & pull request button
#STEP5 : Click Create pull request to open a new pull request