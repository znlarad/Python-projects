#login page
#password generator
#This code is written by znl_arad

import random

def pass_generator():
    import random
    alpabet_list_uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                              "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alpabet_list_lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                              "s", "t", "u", "v", "w", "x", "y", "z"]
    # elements_list = ["_", ".", "#", "*", ]

    number_x = str(random.randint(1, 9))
    number_y = str(random.randint(1, 9))
    alpabet1 = random.choice(alpabet_list_lowercase)
    alpabet2 = random.choice(alpabet_list_lowercase)
    alpabet3 = random.choice(alpabet_list_uppercase)
    alpabet4 = random.choice(alpabet_list_uppercase)
    # element = random.choice(elements_list)
    alpabet5 = random.choice(alpabet_list_uppercase)

    password= (alpabet5 + alpabet1 + number_x + number_y + alpabet3 +  alpabet2  + alpabet4)
    return password
#function now defined
#program starting
while True:
    print("DO YOU HAVE AN ACCONT ?")
    user_input_2 = input("yes or no?")
    user_input_1=user_input_2.lower()
    if user_input_1=="yes" or user_input_1=="no":
        break
    else:
        print("only write (yes) or (no) ")

while True:
    if user_input_1 == "no":
        username = input("write a user name with letters A-Z : ")
        # print(type(username))
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for x in numbers:
            if x in username:
                print("your username should only be letters A-Z")
                break
        else:
             break


user_password = pass_generator()
print("this is your password ", "(", user_password, ")")
print("you have created an acount")
print("now you can login with your information")

while True:
    user_name = input("username : ")
    userr_password = input("password : ")
    if user_name != username or userr_password != user_password:
        print("your username or password is incorect")


    else:
        print("you have logind in ")
    
        break























