k = int(input("Enter k: "))

input_data = open('data/input.in').read().splitlines()   #read input.in
csv_reader = open('data/diabetes.csv').read().splitlines()                   #create variable to store training data
outp = open("output.txt","w")               #create
tdp = open("diabetes-out.csv","w")         #for appending training data
for contents in csv_reader:                 #copy contents of diabetes.csv
    tdp.write(contents+"\n")
