#1)
#deposits = [10, 10, 10, 10, 10]
#def checkBalance(Balance):
#    total = 0
#    for deposit in Balance:
#        total += deposit
#    return total
#print checkBalance(deposits)

#2)
#myList = ['one','big','string']
#def joinStrings(combine):
#    tracker = ''
#    for strings in combine:
#        tracker += strings
#    return tracker
#print joinStrings(myList)

#3)
#myList = [1,2,3]
#def addThis(listOf):
#    feedMe = 0
#    for ints in listOf:
#        feedMe += ints
#    return "The sum of the numbers " + str(listOf) + " is " + str(feedMe)
#print addThis(myList)

#4)
magicNumber = 22
uGuess = input("This is the amazing Guessing Game! You have 10 tries to guess the magic number corectly! ")
def guessingGame(guess):
    count = 1
    while(count <= 10):
        if count == 10:
            return "You've reached the maximum number of attempts! The magic number was " + str(magicNumber)
        elif guess ==  magicNumber:
            return "You guessed correctly!"
        else:
            count += 1
            if guess > magicNumber:
                print "Nope, try again. You guess is higher than the magic number."
                guess = input("Input your next guess ")
            elif guess < magicNumber:
                print "Nope, try again. You guess is lower than the magic number."
                guess = input("Input your next guess ")
print guessingGame(uGuess)
/
#5)
#week = ("Monday", "Tuesday", "Wednsday", "Thursday", "Friday")
#course = ["Pre Calc", "Hip Hop", "Pe Calc", "Hip Hop", "Pre Calc"]
#def favClass(day, myClass):
#    placeHolder = zip(day, myClass)
#    for x,y in placeHolder:
#        print x, ": ", y #comma is the same as conca
#favClass(week, course)

#6)
#for num in range(0,20):
#    print "up"
#    print "down"
#    print x+1

#7)
#for num in range(0,input("How many times do you want to say \"Hello\"? ")):
#   print "Hello"

#8)
#myList = ['a', 'b', 'c', 'd']
#def sortThis(inputList):
#    counter = 1
#    for element in inputList:
#        print "Item " + str(counter) + ": " + element
#        counter+=1
#myList.append('e')
#myList.append('f')
#sortThis(myList)


#9)
#rby = ["Red", "Blue", "Yellow"]
#def primeColour(myList):
#    count = 0
#    for x in myList:
#        count+=1
#        print x + " is a primary colour."
#    print count
#primeColour(rby)

#10)
#num = 20
#while num <=50:
#    print num
#    num+=1


#11)
#num = 1
#while num<=20:
#    print num
#    num+=1


#12)
#Fix


#13)
#x = input("Input a number. ")
#def halfie(num):
#    while num>=0.0: #and not(x<0):
#        if num%2==0:
#            print str(num) + " is even."
#            num -= .5
#        else:
#            print str(num) + " is odd."
#            num -= .5
#halfie(x)

#14)
#def giveMeTen(x):
#    while x<=10:
#        if x%2==0:
#            print str(x) + " is even."
#            x+=1
#        else:
#            print str(x) + " is odd."
#            x+=1
#giveMeTen(0)


#15)
#User inputs dollar amount
#Break down into quarters first, then nickles, then cents
#Use multiples of quarters that is less than the dollar amount. Then use multiples of nickles, and then cents
#dAmount = input("Input a dollar amount you would like converted into change $")
#def makeChange(amount):
#    quarters = 0
#    nickles = 0
#    pennies = 0
#    quarters,remainder = divmod(amount,0.25)
#    if remainder != 0:
#        nickles, remainder = divmod(remainder,0.05)
#        if remainder != 0:
#            pennies, remainder = divmod(remainder, 0.01)
#    return "$" + str(dAmount) + " to change is " + str(quarters) + " quarters, " + str(nickles) + " nickles, and " + str(pennies) + " pennies." 
#print makeChange(dAmount)


























































































































































