# Import the random module to generate random numbers
import random 

# Initialize the level counter, starting at level 1
level_counter = 1 

# Print the welcome message
print ("""
Welcome to Feeling Lucky. A game to test if today truly is your lucky day. 
Simply follow the prompts and test your luck \U0001F44C""") 

# Main game loop, this runs until the player has completed all 10 levels
while level_counter < 11:
    i = level_counter # Store the current level number in variable 'i'
    bad_value = False # Flag to track if the user has entered a non integer value
    print(  """
          
level:""", i)     # Print the current level number
    lucky_numbers = []# Initialize an empty list to store lucky numbers
    
    # Generate a list of random lucky numbers
    # The number of lucky numbers decreases as the level increases
    while len (lucky_numbers) != (11 - i):
        added_number = random.randrange(1,11) # Generate a random number between 1 and 10
        if added_number not in lucky_numbers: # Ensure no duplicate numbers in the list
            lucky_numbers.append(added_number) # Add the unique number to the list

    # Prompt the user to choose their lucky number  
    print ("Choose your lucky number from 1-10: \U0001F340 ")
    user_value = input() # Get input from the user
    # Check if the input is a digit
    if user_value.isdigit():
        user_value = int (user_value) # Convert the input to an integer if it's a digit
    else:
        # If the input is not a digit, reset the game and start from level 1
        print("That is not a digit. \U0001F621 Back to the start")
        level_counter = 1
        continue # Restart the loop

    # Validate that the user's input is within the range 1-10
    while user_value > 10 or user_value < 1:
            # If the input is out of range, prompt the user to enter a valid number
        print ("\U0001F928 Value not in the range of 1-10. Please choose your lucky number from 1-10: ")
        user_value = input() # Get a new input from the user
        check_user_value = user_value
        if user_value.isdigit(): # Convert the input to an integer if it's a digit
            user_value = int (user_value)
        else:
            bad_value = True # If input is not a digit, set bad_value to True
            break # Exit while loop

    # If a bad value was entered, reset the game and start from level 1
    if bad_value == True:
        print ("That is not a digit. \U0001F621 Back to the start")
        level_counter = 1
        continue # Restart the loop
            
    # Check if the user's chosen number is in the list of lucky numbers
    if user_value in lucky_numbers and level_counter == 10:
         # If the user wins on the final level, congratulate them
        print ("You won, today is your lucky day. You should probably buy a lottery ticket \U0001F3B0")
        level_counter+= 1 # Move to the next level (this ends the game)
    elif user_value in lucky_numbers:
        # If the user wins on any other level, advance to the next level
        print ("\U0001F44F Congratulations, You are going on to the next level")
        level_counter+= 1 # Increase the level counter
    else:
        # If the user does not pick a lucky number, reset the game and start from level 1
        print ("Unlucky, Back to day one for you \U0001F480")
        level_counter = 1 # Reset the level counter