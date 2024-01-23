## string concatenation 
'''
name = "Ryunosuke"

print("subscribe to " + name)
print("subscribe to {}".format(name))
print(f"subscribe to {name}")
'''
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous person: ")

madlib = f"Computer programming is so {adj}! It make me so exicited all the time becasue \
I love {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)