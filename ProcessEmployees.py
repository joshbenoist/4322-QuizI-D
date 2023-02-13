'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

infile = open("employee_data.csv", "r")


#create an empty dictionary

dict = {}
new_dict = {}

#use a loop to iterate through the csv file
#check if the employee fits the search criteria

with open("employee_data.csv", "r") as a:

    reader = csv.reader(a)

    for row in reader:
        Department = row[3]
        Title = row[4]
        fname = row[1]
        lname = row[2]
        salary = float(row[5])

        if Department == "Marketing":
            if Title == "CSR":
                key = fname, lname
                dict[key] = salary,
                new_sal = salary * 1.1
                new_dict[key] = new_sal

    

print(dict)
print('=========================================')
print(new_dict)

#iternate through the dictionary and print out the key and value as per printout



          
        

        
    


