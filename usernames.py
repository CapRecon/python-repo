username_taken = None #boolean to check if username has been taken
username_array = [] #array to store all usernames.
while True: #this loop runs infinitely until the exit condition is verified
    username = input("Please enter your username. ") #this code takes username input from the user.
    if username.lower() == "done": #the exit condition of the code
        print("Exiting username creation....") #program exits if username entered is 'done'
        break
    elif len(username) < 5: #only usernames between 5 and 25 characters acceptable.
        print(f"Username '{username}' is less than 5 characters long.")
        print("Please try again.")
        continue
    elif 25 >= len(username) >= 5:
        if len(username_array) > 0: #runs for loop with variable 'indexer'
            for indexer in username_array:
                if indexer == username: #if the indexer is equal to the username
                    print(f"'{username}' has already been taken.") #returns an error and asks for another input
                    print("Please try again.")
                    username_taken = True
                else:
                    continue
            if not username_taken: #otherwise it accepts the username 
                print(f"{username} accepted.") 
                username_array.append(username) #the username is appended to the array
            else:
                continue
        elif len(username_array) == 0: #if the array is already empty, will accept the
            print(f"{username} accepted.") #first username by default
            username_array.append(username)
    elif len(username) > 25:
        print(f"'{username}' is more than 25 characters long.")
        print("Please try again.")
        continue
view_array = input("Would you like to view all entered usernames? (Y/N) ") #displays the array after
if view_array.lower()[0] == "y": #exiting the loop if user asks 
    print(username_array)
else:
    print("Exiting...")
