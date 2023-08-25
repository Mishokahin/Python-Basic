mammals = ["dog"]
reptiles = ["crocodile", "tortoise", "snake"]
animal = input()

if animal.lower() in mammals:
    print("mammal")
elif animal.lower() in reptiles:
    print("reptile")
else:
    print("unknown")