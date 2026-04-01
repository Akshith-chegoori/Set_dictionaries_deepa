marks = {'Ravi': 72, 'Priya': 91, 'Arjun': 65, 'Meena': 85}
#Print Priya's marks
print(f"Priya's marks:{marks['Priya']}")


# Update Arjun's marks to 70
marks['Arjun']=70
print(marks)



#Add a new student 'Kiran': 88
marks['Kiran']=88
print(marks)



#Delete Ravi's entry
del marks['Ravi']



#Print the final dictionary
print(f"the final dictionary:{marks}")

