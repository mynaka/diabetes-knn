k = int(input("Enter k: "))

input_data = open('data/input.in').read().splitlines()   #read input.in
csv_reader = open('data/diabetes.csv').read().splitlines()                   #create variable to store training data
outp = open("output.txt","w")               #create
tdp = open("diabetes-out.csv","w")         #for appending training data
for contents in csv_reader:                 #copy contents of diabetes.csv
    tdp.write(contents+"\n")
row = []
trainingRow = []
for input_row in input_data:
    k_neighbors = []                                #empties/declares k_neighbors array
    row = input_row.split(",")                      #input files are split by the delimiter ","
    for csv_row in csv_reader:
        distance = 0
        trainingRow = csv_row.split(",")
        for i in range(len(row)):
            distance+=((float(row[i])-float(trainingRow[i]))**2)            #calculate distance
        distance = math.sqrt(distance)

        #code for remembering k lowest distance
        k_neighbors.append([distance, trainingRow[-1]])                 #appends a 2-element array containing distance and class
        k_neighbors = sorted(k_neighbors)                               #sorts array by distance
        if(len(k_neighbors) > k):                                       #if length of array is greater than k,
            k_neighbors.pop(-1)                                         #last element(with highest distance) is popped

        classes = [i[1] for i in k_neighbors]                           #counts classes by first compiling them in a list
        mode = max(classes, key=classes.count)                     #then uses a max() function to look for the mode
    outp.write(input_row+','+('Diabetic' if(mode=='1') else 'Non-Diabetic')+"\n")
    tdp.write("\n"+input_row+','+mode)
