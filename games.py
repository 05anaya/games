import random

# defining a function for the game rock paper scissors
def rpas():
    # making a list to store rock paper scissors
    rps = ["rock", "paper", "scissors"]
    # displaying a welcome message 
    print("Welcome to Rock, Paper, Scissors! Play the game against the computer.")
    print()

    # asking the user for the input 
    inp = input("Enter your input (rock, paper, or scissors): ").lower()
    # chosing a random element from the list rps 
    g = random.choice(rps)

    # comparing the users input and displaying the results

    if inp == "rock":
        if g == "scissors":
            print("Computer played scissors. You win! :)")
        if g == "paper":
            print ("Computer played paper. You lose. :(")
        if g == "rock":
            print ("Computer played rock. Tie.")

    elif inp == "paper":
        if g == "rock":
            print("Computer played rock. You win! :)")
        if g == "scissors":
            print ("Computer played scissors. You lose. :(")
        if g == "paper":
            print ("Computer played paper. Tie.")

    elif inp == "scissors":
        if g == "paper":
            print("Computer played paper. You win! :)")
        if g == "rock":
            print ("Computer played rock. You lose. :(")
        if g == "scissors":
            print ("Computer played scissors. Tie.")

    # printing an error message 
    else:
        print ("Invalid input.")  

# defining a function for the quiz game 
def quiz():
    # creating a dictionary to store the questions and the answers 
    questions = {1:"Which country has the tallest mountain in the world?",
             2:"What is the fastest land animal?",
             3:"Which state in india has the largest coastline?",
             4:"What is the fifth planet from the Sun?",
             5:"Do jellyfish have brains? (yes/no)",
             6:"What is the longest river on the Earth?",
             7:"Which element are diamonds made of?",
             8:"In which country is the Eiffel Tower?",
             9:"What force pulls objects towards the Earth?",
             10:"Which country has the most lakes in the world?"}
    answers = {1:"nepal", 2:"cheetah", 3:"gujarat", 4:"jupiter", 5:"no",
            6:"nile", 7:"carbon", 8:"france", 9:"gravity", 10:"canada"}

    score = int(0)
    n = int(1)

    # displaying the welcome message
    print("Welcome to the Quiz Game! This game has 10 questions. Try your best to answer them correctly. All the answers are single word answers.")
    print()

    # 
    while n <=10:
        print(questions[n])
        ans = input("Answer- ").lower() # converting the answer in lower case 
        if ans == answers[n]:
            print("The answer is correct!")
            score+=1
        else:
            print("Sorry, your answer is wrong. The correct answer is", answers[n])
        n+=1 

    print()
    # printing the result
    print("Your score is", score, "out of 10.")

# defining a function for the game, number guessing
def num_guessing():
    # displaying a welcome message
    print("Welcome to number guessing game!")
    # asking the user to  input the lower and the higher bound of the range
    low = int(input('Enter the lower bound number of the range: '))
    high = int(input('Enter the higher bound number of the range: '))
    # calculating the difference of the lower and higher bound 
    diff = high - low
    
    # if the difference the less than 10 
        # displaying an error message 
        # and asking for the input again
    if diff < 10:
        print('The differnce of th elower and higher bound should be at least 10')
        low = int(input('Enter the lower bound number of the range: '))
        high = int(input('Enter the lower bound number of the range: '))

    # generating a random number from the given range
    num = random.randint(low,high)
    print(num)
    print("You have 5 chances to guess")
    # initializing count as 0
    count = 0 

    # while the count is less than 5 
         # asking for user input
         # if user input = the randomly genrated no. 
            # printing the results
         # if the user i/p is greater than or less than the randomly generated no.
            # printing a hint 
         # if the count is 5 
            # printing a ' game over' message
    while count < 5:
        guess = int(input('Guess the number: '))

        if guess == num:
            print("You guessed the number!")
            print(f"The number of turns you used: {count+1}")
            break
        elif guess < num:
            print("oops! try putting a higher value")
        elif guess > num:   
            print("oops! try putting a lower value")
        count += 1

    if count == 5:
        print("game over") 

# defining a function for the gane of madlibs
def madlibs ():
        # displaying a welcome message
        print("Hello!Lets play mad libs")
        # asking the user for the input
        user_ip = int(input("please choose a number from 1 - 3: "))

        # making a functions for all 3 paragragraphs 
            # asking for all inputs from user
            # displaying the output along with the input
        def para1 ():
            ip_1 = input('Enter a name: ')
            ip_2 = input('Enter an adjective: ')
            ip_3 = input('Enter an adjective: ')
            ip_4 = input('Enter a noun: ')
            ip_5 = input('Enter an adjective: ')
            ip_6 = input('Enter a noun: ')
            ip_7 = input('Enter an adjective: ')
            ip_8 = input('Enter an adjective: ')
            ip_9 = input('Enter a verb: ')
            ip_10 = input('Enter a verb: ')
            ip_11 = input('Enter a name: ')
            ip_12 = input('Enter a verb: ')
            ip_13 = input('Enter an adjective: ')
            ip_14 = input('Enter a verb: ')
            
            print("TRIP TO THE PARK")
            print(f"Yesterday,{ip_1} and I went to the park. On our way to the {ip_2} park,we saw a {ip_3} {ip_4} on a bike. We also saw big {ip_5} balloons tied to a {ip_6}")
            print(f"Once we got to the {ip_7} park,the sky turned {ip_8}. It started to {ip_9} and {ip_10}. {ip_11} and I {ip_12} all the way home.Tommorow  we'll try to go to the {ip_13} park again and hope it doesn't {ip_14} ")

        def para2 ():
            ip_1 = input('Enter an adjective: ')
            ip_2 = input('Enter an adjective: ')
            ip_3 = input('Enter a noun: ')
            ip_4 = input('Enter an animal: ')
            ip_5 = input('Enter a vegetable: ')
            ip_6 = input('Enter a vegetable: ')
            ip_7 = input('Enter a colour: ')
            ip_8 = input('Enter an adjective: ')

            print("LUCH ROOM!")
            print(f"Make sure your lunch box is filled with nutritious {ip_1} food. Do not go to the {ip_2} food stand across the street from school.")
            print(f"The hamburgers they serve are fried in {ip_3} and are made of {ip_4} meat.So take a sandwich made of {ip_5} or {ip_6} it's much healthier! Drink {ip_7} milk instead of {ip_8} colas.")

        def para3 ():
            ip_1 = input('Enter a noun: ')
            ip_2 = input('Enter an adjective: ')
            ip_3 = input('Enter a noun: ')
            ip_4 = input('Enter a noun: ')
            ip_5 = input('Enter a noun: ')
            ip_6 = input('Enter a noun: ')
            ip_7 = input('Enter a tool: ')
            ip_8 = input('Enter a noun: ')
            ip_9 = input('Enter a noun: ')
            ip_10 = input('Enter an adjective: ')

            print("SPRING GARDEN")
            print(f"Planting a vegetable garden is not only fun, it also helps save {ip_1}. You will need a piece of {ip_2} land. You may need a  {ip_3} to keep the {ip_4} and {ip_5} out.")
            print(f"As soon as {ip_6} is here you can go out there with your {ip_7} and plant all kinds of {ip_8}.Then in a few months, you will have corn on the {ip_9} and big,{ip_10} flowers.")
        
        # calling the function according to the user's choice
        if user_ip == 1:
            para1()
        
        elif user_ip == 2:
            para2()
        
        elif user_ip == 3:
            para3()

        else:
            print('Invalid input')

 # defining the main function   
def main ():
    # asking user for the choice of the game 
    print("Hello!")
    print("Which game would you like to play?")
    print("Choose:")
    print("1 to play rock,paper,scissors")
    print("2 to play madlibs")
    print("3 to play quiz")
    print("4 to play guess the number")
    c = 0
    ch = int(input('Please enter your choice: '))

    while c >= 0 and c < 3:
        if ch == 1:
            rpas()
        elif ch == 2:
            madlibs() 
        elif ch == 3:
            quiz()
        elif ch == 4:
            num_guessing()    
        else:
            print("Invalid input")

        print("Do you want to continue this game or play a new game or quit?")
        print("Please Enter \n 1 to continue \n 2 for new game \n 3 to quit")
        c = int(input('please enter your choice: '))

        if c == 2:
            print("Choose:")
            print("1 to play rock,paper,scissors")
            print("2 to play madlibs")
            print("3 to play quiz")
            print("4 to play guess the number")
            ch = int(input('Please enter your choice: '))
# calling main function
main()   