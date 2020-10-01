#this is menu driven Program
import pyttsx3
import os
pyttsx3.speak("Hello sir")
print("enter here")
p = input("")
pyttsx3.speak("how are you")
# enter i am fine
reply = input("")
if ("fine" in reply):
    pyttsx3.speak("that's good sir")
pyttsx3.speak("how can i help you")
# enter what can you do for me
help = input("")
if ("for" in help):
    pyttsx3.speak("i can do many thing for you ")
# enter tell or introduces yourself
intro=input("")
if("introduces" in intro) or("tell" in intro):
    pyttsx3.speak("my name is Gaurav and i am your assistant ")
# enter show me the list of task that you can do me
task=input("")
if("show" in task) or ("list" in task):
    pyttsx3.speak("ofcourse sir")
    print(" I can do these thing:\n"
             "1:open notepad\n"
             "2:can show menu for food\n"
             "3: can open camera\n"
             "4: can open calculator\n"
             "5: can open vlc player for you"
              )
p=input("")
if ("notepad" in p):
    pyttsx3.speak("ok i lunch just a minute")
    os.system("notepad")
# enter can you order food for me
elif("order" in p) or ("food" in p):
    pyttsx3.speak("ofcourse sir tell me what you want to eat")
    print(" Pizza World: 1")
    print(" Sandwich: 2")
    print(" Pasta: 3")
    print(" Burger Farm House: 4")

    dish = int(input(""))
    if int(dish == 1):

        print("Tandoori Pizza :Rs 200"),
        print("Cheese Garlic Pizza :Rs150"),
        print("Mashroom Pizza :Rs120"),
        print("Capsicum Onion Pizza :Rs100")
    elif (dish == 2):

        print("Veg Sandwich :Rs40")
        print("Grilled Sandwich :Rs50")
        print("Cheese Sandwich :Rs80")
        print("Special Sandwich :Rs100")

    elif (dish == 3):

        print("Red sos Pasta :Rs90")
        print("White sos Pasta :Rs110")

    elif (dish == 4):
        print("Aloo tikki Burger :Rs50")
        print("Cheese Burger :Rs60")
        print("Grilled Burger :Rs45")
        print("Paneer Burger :Rs80")

elif("camera" in p):
    pyttsx3.speak("ok i lunch just a minute")
    os.system("camera")
elif("calculator" in p):
    pyttsx3.speak("ok i lunch just a minute")
    os.system("calculator")

elif("video player" in p) or ("vlc player" in p):
    pyttsx3.speak("ok i lunch just a minute")
    os.system("vlc")
else:
    print("invalid")
