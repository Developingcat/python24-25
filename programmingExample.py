print("############################################")
print("############################################")
print("###        Programming Example           ###")
print("############################################")
print("############################################")



favoriteColor = input("What's your favorite color? ") #Put in blue for now 
print("Dog, Cat, Lion, Tiger, Rabbit, Bird, Dolphin, Elephant, Sloth, Turtle")
favoriteAnimal = input("What's your favorite animal from this list? ")


# if favoriteColor == "blue" and favoriteAnimal == "Dog": 
#     print("Your favorite color is blue, and your favorite animal is a dog! Let's see what this says about you..\n")
#     print("You're a kind-hearted and loyal individual who probably really likes it when you're friends give you food they don't want, good on you!")
# elif favoriteColor =="blue" and favoriteAnimal == "Cat":
#     print("Your favorite color is blue, and your favorite animal is a cat....let's see what that says about you.\n")
#     print("You find it easy to nap pretty much anywhere, only people who really know you know you're nice, you find it tough to make friends. I'm sorry to hear that.")

if favoriteColor == "blue" and favoriteAnimal == "dog":
 print("Your favorite color is blue, and your favorite animal is" ,str(favoriteAnimal), "let's see what that says about you..")
 print("You're a kind-hearted and loyal individual who probably really likes it when you're friends give you food they don't want, good on you!")
elif favoriteAnimal == "cat":
 print("Your favorite color is blue, and your favorite animal is" ,str(favoriteAnimal), "let's see what that says about you..")
 print("You find it easy to nap pretty much anywhere, only people who really know you know you're nice, you find it tough to make friends. I'm sorry to hear that.")
elif favoriteAnimal == "lion" or favoriteAnimal == "tiger":
 print("Your favorite animal is" ,str(favoriteAnimal), "let's see what that says about you..")
 print("You're courageous and intelligent! Your friends probably feel like they can go to you if someone is giving you trouble and you'll be able to help with the situation. You probably confront bullies a lot. Good on you!")
elif favoriteAnimal == "rabbit":
 print("Your favorite color is blue and your favorite animal is" ,str(favoriteAnimal), "let's see what that says about you..")
 print("Easily startled, but very quick on your feet! In most confrontative situations, you tend to behave more flight than you do fight, however, you're very quickly adaptable and you tend to get from one place to another no problem at all!")
elif favoriteAnimal == "bird" or favoriteAnimal == "dolphin":
 print("Your favorite animal is" ,str(favoriteAnimal), "let's see what that says about you..")
 print("Emotionally carefree, you tend to go with wherever the day takes you! No matter how bad it is, you're always managing to make it somehow bright and colorful, good on you!")
elif favoriteAnimal == "elephant": 
 print("Your favorite animal is" ,str(favoriteAnimal), "let's see what that says about you..")
 print("Strong on emotional intelligence, your friends probably turn to you when they need advice on relationships or friendship and somehow you've always got the answer for them no matter the situation, you probably also carry snacks on you and are one of the nicest people ever.")
elif favoriteAnimal == "sloth" or favoriteAnimal == "turtle": 
 print("Your favorite animal is" ,str(favoriteAnimal), "let's see what that says about you..")
 print("You more value taking your time with things over rushing through every thing. Your favorite story is probably the tortoise and the hare and it's a philosphy you live by, you also most definately own a camera and enjoy capturing the little moments to look back on later. ")