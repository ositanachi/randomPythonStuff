#Dictionaries (another type. Tupples = Parenthesis. List = Brackets. Dictionaries = Curly braces 
classBirthdays = {"John":"January", "Tyrone":"March"}
#Access a value in a dictionary but calling the 'key'
#print classBirthdays["John"]
#Updating the value associated with the key John
classBirthdays["John"] = "September"
#print classBirthdays["Tyrone"]
#del classBirthdays["Tyrone"]
#print classBirthdays

#To get keys .keys() function
#i.e. variable_name.keys()

#To get values .values() function
#i.e. variable_name.values()

#Access keys using .keys() function
print classBirthdays.keys()

#Get values using .values() function
print classBirthdays.values()

#Use the built in function len(list) to find the length of a dictionary. 
print len(classBirthdays)

#Iterating over a list
for name in classBirthdays:
    print name, " was born in ", classBirthdays[name]

#The items() method gets a list of tuples
for name, month in classBirthdays.items():
    print name, " was born in ", month


#Next Thursday, April 30th 11 to 1    




#Create a list clled month that contains the months of the year.
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

#Declaring a dictionary
classBirthdays = {}

#Adding a value to a dictionary
name = raw_input("Please enter your name. \n")
b_month = input("Please enter the numerical value of your birth month (1-12). \n")

#Square bracket to access the name that was inputted
classBirthdays[name] = month[b_month-1]

print classBirthdays





