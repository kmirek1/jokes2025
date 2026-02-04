


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes


    


def start():
     answer = input("Do you want to hear a joke? ").lower()
     if answer == "no":
        print("Okay suit yourself!")
     elif answer == "yes":
        print("Great, let's play!")
        joke_topic()

def rating():
    rate = int(input("Please rate our game 1-10! "))
    print(f"User Satisifaction: {rate * 10}%")
    if rate > 6:
        print("Glad you liked it!")
    else:
        print("Sorry you didn't like")




def joke_topic():
     topics = ["robbers", "tanks", "pencils" ]
     topic = input("Do you want to hear a joke about robbers, tanks, or pencils?").lower()
     
     if topic == "robbers":
        input("Knock Knock ")
        input("Calder")
        print("Calder police - I've been robbed!")
     elif topic == "tanks":
        input("Knock Knock ")
        input("Tank ")
        input("You are welcome! ")
     elif topic == "pencils":
        input("Knock Knock ")
        input("Broken pencil ")
        input("Nevermind, it's pointless! ")
     else:
        print("Sorry I'm not funny enough to know that...")
        return joke_topic()
     
     exit()

def exit():
     joke = input("Do you want to hear another joke? ").lower()
     if joke == "no":
          rating()
     else:
        joke_topic()
start()