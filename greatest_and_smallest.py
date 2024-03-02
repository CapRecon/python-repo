#code that takes user input in an array and identifies
#the gretest and smallest numbers.
largest = None #will store the value of the largest number
smallest = None #will store the vlaue of the smallest number
numlist = [] #this array will store all the entered numbers
while True: #an infinite loop with try and except for error handling
    try:
            n = input("Enter a valid number ") #takes input from the user
            if n == 'done': #if user inputs 'done'
                break #the loop exits
            elif n != 'done': #for any other input
                num = int(n) #the integer value of the input is stored in num
                numlist.append(num) #num is appended into the array
    except: #if the input can't be converted to int, runs except
        print("Invalid input") 
        continue
print(numlist) #the numlist is printed afer exiting loop
largest = None
smallest = None
for current_num1 in numlist: #runs for loop that scans over the input
     if largest == None: #stores largest number in the array in largest
          largest = current_num1
     elif current_num1>largest:
          largest = current_num1
print("Maximum is",largest) #prints largest number 
for current_num2 in numlist: #runs another loop over the input
     if smallest == None: #stores smallest number in the array in smallest
          smallest=current_num2
     elif current_num2 < smallest:
          smallest = current_num2
print("Minimum is", smallest) #prints the smallest number