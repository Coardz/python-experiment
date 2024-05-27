# Write your solution here

#ask for character name input
name = str(input("Please type in your name:"))

#donald duck nephews Huey, Dewey or Louie
#mickey mouse nephew Morty or Ferdie
if (name == "Huey" or name == "Dewey" or name == "Louie"):
    print("I think you might be one of Donald Duck's newphews.")
elif (name == "Morty" or name == "Ferdiie"):
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a newphew of any character I know of.")