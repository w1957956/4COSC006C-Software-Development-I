# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student Name: Mohamed Ayyub Hameem
# Student ID: 20211374/ w1957956

# Date: 06/11/2022

List = []
#Assigning variables for counting progression
Progress = 0
Trailer = 0
Retriever = 0
Exclude = 0
decision = 'y'
List = []
File = open("Results.txt", "w")

#Creating a loop therefore the user can enter data of another student
#Validating the student credit score and using a user-defined function
while decision == 'y':
    x = True
    while True: 
        def Credit_Level(a):
            while True:
                try:
                    x = int(input("Please enter your credits at"+" "+a+" "+": ")) #Accepts only 0,20,40,60,80,100,120
                    if x < 0 or x > 120 or (x % 20) != 0:
                        print("Out of range")
                        print('')
                    else:
                        break       
                except ValueError:
                    print("Integer required")
                    print('')               
            return x
  
        Pass = Credit_Level("PASS")
        Defer = Credit_Level("FAIL")
        Fail = Credit_Level("DEFER")
        
#Validating the total student credit score
        Total = Pass + Defer + Fail
        if Total != 120:
            print("Total incorrect.")
            print('')    
        else: break
        
#Using IF statements to predict progression outcomes, appending files into a list, writing data into a file and entering data into a nested dictionary        
    if Pass == 120:   
        print ("Progress")
        Progress = Progress + 1
        A = "Progress  - {}, {}, {}".format(Pass,Defer,Fail)
        List.append(A)
        File.write(A+"\n")
        print('')
        while x == True:
            decision = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            print('')
            if decision == 'q':
                break
            elif decision == 'y':
                x = False
        
    elif Pass == 100: 
        print ("Progress(module trailer)")
        Trailer = Trailer + 1
        A = "Progress(module trailer) - {}, {}, {}".format(Pass,Defer,Fail)
        List.append(A)
        File.write(A+"\n")
        print('')
        while x == True:
            decision = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            print('')
            if decision == 'q':
                break
            elif decision == 'y':
                x = False
        
       
    elif -1 < Pass < 81 and Fail < 80:  
        print ("Do not Progress – module retriever")
        Retriever = Retriever + 1
        A = "Module retriever - {}, {}, {}".format(Pass,Defer,Fail)
        List.append(A)
        File.write(A+"\n")
        print('')
        while x == True:
            decision = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            print('')
            if decision == 'q':
                break
            elif decision == 'y':
                x = False

    else:
        print ("Exclude")
        Exclude = Exclude + 1
        A = "Exclude - {}, {}, {}".format(Pass,Defer,Fail)
        List.append(A)
        File.write(A)
        print('')
        while x == True:
            decision = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            print('')
            if decision == 'q':
                break
            elif decision == 'y':
                x = False
                        
File.close()

#Printing the number of outcomes as stars using a user-defined function to form a histogram
print('---------------------------------------------------------------')     
print('Histogram')

def Stars(x):
    for i in range(x):
        print('*',end='')

print("Progress ",Progress,": ",end=" ")
Stars(Progress)
print(" ")
print("Trailer  ",Trailer,": ",end=" ")
Stars(Trailer)
print(" ")
print("Retriever",Retriever,": ",end=" ")
Stars(Retriever)
print(" ")
print("Exclude  ",Exclude,": ",end=" ")
Stars(Exclude)
print("\n")
Outcomes = Progress + Trailer + Retriever + Exclude
print(Outcomes,"outcomes in total")
print('---------------------------------------------------------------')

#Part 2(Extension)
print(" ")
print("Part 2: ")
for i in List:
    print(i)

#Part 3(Extension) #Printing the outcomes from a text file
print(" ")
print("Part 3: ")
File = open("Results.txt", "r")
Lines = File.read()
print(Lines)
File.close()


#References:
#Inserting values into strings : https://matthew-brett.github.io/teaching/string_formatting.html
