import random
random_phrase = ["That's in right now.", "That's so stylish!", "That's cool!", "Wow! Nice choice!"]

name = input("What is your first name?: ")
print("Nice to meet you, " + name + "!")

clothes = input("\nLet's talk fashion! Do you like dresses or jeans more? ")

if clothes.lower() == "dresses":
    print(random_phrase[random.randint(0,3)] + " Dresses are pretty neat! They're really pretty.")
elif clothes.lower() == "jeans":
    print(random_phrase[random.randint(0,3)] + " Jeans are really cool! They're comfy.")
else:
    print("...I don't think that was one of the options.")

shoes = input("\nWhat kind of shoes do you like, " + name + "? ")

if shoes.lower() == "converse" or shoes.lower() == "sneakers":
    print("Nice! Comfort is always a must! " + random_phrase[random.randint(0,3)])
elif shoes.lower() == "sports" or shoes.lower() == "tennis shoes" or shoes.lower() == "tennis":
    print("That's cool! Sporty shoes are comfortable. " + random_phrase[random.randint(0,3)])
else:
    print("That's pretty nice, sounds cool! " + random_phrase[random.randint(0,3)])

age = int(input("\nWhat's your age? "))
if age <= 12:
    print("That's a pretty young age to explore style. Good luck!")
elif age <= 14:
    print("That's a decent age to start exploring style! Good luck!")
elif age <= 24:
    print("That's a good age to start exploring style!")
else:
    print("Never too late to start exploring your style!")

hat = input("\nWell! What kinds of accessories do you like? Let's start with head accessories! Do you like bows or caps more? ")
if hat.lower() == "bows":
    print("Bows are cute! They're very pretty." + random_phrase[random.randint(0,3)])
elif hat.lower() == "caps":
    print("Caps are pretty cool! " + random_phrase[random.randint(0,3)])
else:
    print("Well, that's understandable!")

style = input("\nWell, do you prefer cute or cool clothing more? ")
if style.lower() == "cute":
    print(random_phrase[random.randint(0,3)] + " So do I! You have very good taste.")
elif style.lower() == "cool":
    print("That's nice! It does look cool and comfortable. " + random_phrase[random.randint(0,3)])

thoughts = input("\nWell, is there anything else to add? ")
print("\nWell, then! It was quite fun talking to you about fashion, " + name + "!")