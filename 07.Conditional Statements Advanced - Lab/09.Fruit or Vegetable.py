fruit = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetable = ["tomato", "cucumber", "pepper", "carrot"]

produce = input()

if produce in fruit:
    print("fruit")
elif produce in vegetable:
    print("vegetable")
else:
    print("unknown")