# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student Name: Mohamed Ayyub Hameem
# Student ID: 20211374/ w1957956

# Date: 06/11/2022

Progress = 0
Trailer = 0
Retriever = 0
Exclude = 0
decision = 'y'
#Using an empty dictionary to enter different student IDs as a nested dictionary
mydict = {};

#Creating a loop therefore the user can enter data of another student 
while decision == 'y':
    x = True
    while True:
        ID = input("Enter Student ID: ")
        if list(ID) == [] or ID[0] != "w" or len(ID) != 8:
            print("Invalid student ID!Please enter correct 8 charcter ID beginning with 'w'.")
            print("eg: w1957956\n")
        else: break 
#Validating the student credit score and using a user-defined function
    while x == True:
        def Credit_Level(a):
            while True:
                try:
                    x = int(input("Please enter your credits at"+" "+a+" "+": "))
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
        
#Using IF statements to predict progression outcomes, appending files into a list and writing data into a file            
    if Pass == 120:   
        print ("Progress")
        Progress = Progress + 1
        A = "Progress  - {}, {}, {}".format(Pass,Defer,Fail)
        mydict[ID] = A
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
        mydict[ID] = A
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
        mydict[ID] = A
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
        mydict[ID] = A
        print('')
        while x == True:
            decision = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            print('')
            if decision == 'q':
                break
            elif decision == 'y':
                x = False

print("Part 4: ") 
result = '\n'.join(f'{key} : {value}' for key, value in mydict.items())
print(result)

#References:
#Python Nested Dictionary : https://www.programiz.com/python-programming/nested-dictionary
#https://stackoverflow.com/questions/40071006/python-2-7-print-a-dictionary-without-brackets-and-quotation-marks
