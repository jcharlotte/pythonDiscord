def say_hi(name):
        if name == '':
            print("You didn't enter your name!")
        else :
            print("Hi there...")
            for letter in name:
                print(letter)

name = input()

say_hi("Charlotte")

def say_hi(name):
    if name == '':
        print("You didn't enter your name!")
    else :
        print("Hi there", name, "!")

say_hi("Charlotte")