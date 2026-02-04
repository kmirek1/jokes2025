


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

 #this function allows the game to start and 
def start():
     # Added a name parameter to pass through the game
     name = input("What is your name? ")
     answer = input(f"Hi {name}, do you want to hear a joke? ").lower()
     if answer == "no":
        print("Okay suit yourself!")
     elif answer == "yes":
        print("Great, let's play!")
        joke_topic(name)
#this function lets the user pick what topic the joke will be about
def joke_topic(user_name):
     topics = ["robbers", "tanks", "pencils"]
     print(f"\nOkay {user_name}, we have: {', '.join(topics)}")
     topic = input("Which one do you choose? ").lower()
     #the jokes are listed here 
     if topic == "robbers":
        input("Knock Knock... (Press Enter)")
        input("Calder... ")
        print("Calder police - I've been robbed!")
     elif topic == "tanks":
        input("Knock Knock... ")
        input("Tank... ")
        print("You're welcome!")
     elif topic == "pencils":
        input("Knock Knock... ")
        input("Broken pencil... ")
        print("Nevermind, it's pointless!")
     else:
        print("Sorry, I'm not funny enough to know that one...")
        return joke_topic(user_name)
     exit_game(user_name)
#this function lets the user rate the game once they are done listening to jokes
def rating(user_name):
    rate = int(input(f"Please rate our game 1-10, {user_name}! "))
    print(f"User Satisfaction: {rate * 10}%")
    if rate > 6:
        print("Glad you liked it!")
    else:
        print("Sorry you didn't like it.")
#this function ends the game once the user is finished 
def exit_game(user_name):
     joke = input(f"\n{user_name}, do you want to hear another joke? ").lower()
     if joke == "no":
          rating(user_name)
     else:
        joke_topic(user_name)

start()