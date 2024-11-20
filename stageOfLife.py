
questionName = input("What's your name?")
print("###################################")
questionAge = int(input("How old are you?"))
print("###################################")
print("Hello," + str(questionName), "you are currently " +str(questionAge), "years old.") 


if questionAge <= 8 or questionAge <= 12: 
    print("You are currently in the childhood stage of life.")
elif questionAge >= 13 and questionAge <= 19:
    print("You are currently a teenager.") 
elif questionAge >= 20 and questionAge <= 29: 
    print("You are currently a young adult.")
elif questionAge >= 30 and questionAge <= 55:
    print("You are an adult.")
elif questionAge >= 56 and questionAge <= 65: 
    print("You are a very wise individual.")
elif questionAge >= 65 and questionAge <= 100: 
    print("Retirement.")
else: 
    print("What.")

