import string
command = input()
c_appeared = False
n_appeared = False
o_appeared = False
word = ""
combination = ""


while command != "End":
    if command in string.ascii_letters:
        if command == "c":
            if c_appeared:
                word += str(command)
            c_appeared = True
        elif command == "n":
            if n_appeared:
                word += str(command)
            n_appeared = True
        elif command == "o":
            if o_appeared:
                word += str(command)
            o_appeared = True
        else:
            word += str(command)

    if c_appeared and n_appeared and o_appeared:
        combination += (str(word) + " ")
        c_appeared = False
        n_appeared = False
        o_appeared = False
        word = ""

    command = input()

print(combination)
