#string concatenation (aka how to put strings together)
# suppose we want to create a string 

# youtuber = "" 

# #  a few ways to print
# print("Subscribe to "+youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")


adj =  input("Ajective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all \
the time because I love to {verb1}. Stay hydrated and {verb2} like \
you are {famous_person}"

print(madlib)