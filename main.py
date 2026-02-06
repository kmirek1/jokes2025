


def rating(user_name):
        rate = int(input(f"\nPlease rate our game 1-10, {user_name}! "))
        print(f"User Satisfaction: {rate * 10}%")
        if rate > 5:
            print("Glad you liked it!")
        else:
            print("Sorry you didn't like it. We'll try harder next time!")

# Function to handle the joke logic with a loop for iteration
def play_jokes(user_name):
    playing = True
    
    while playing:
        topics = ["robbers", "tanks", "pencils"]
        print(f"\nOkay {user_name}, we have: {', '.join(topics)}")
        topic = input("Which one do you choose? ").lower()

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
            add_joke = input("Would you like to add this joke?")
            if add_joke == "yes":
                 new_who = input("What is the joke about?")
                 new_punchline = input("What is the punchline?")
                 topics[topic] = (new_who, new_punchline)
            continue # Restarts the loop to ask for a valid topic

        # This section handles the iteration (looping again or stopping)
        choice = input(f"\n{user_name}, do you want to hear another joke? (yes/no) ").lower()
        if choice != "yes":
            playing = False
    
    rating(user_name)

# Starting function
def start():
    name = input("What is your name? ")
    answer = input(f"Hi {name}, do you want to hear a joke? (yes/no) ").lower()
    
    if answer == "yes":
        print("Great, let's play!")
        play_jokes(name)
    else:
        print("Okay suit yourself! Have a nice day.")

# Call the start function
start()