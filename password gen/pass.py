import random
print ("if you would like a password please press 1 the max your password can be is 74 characters")
print ("if you would like to copy a password please press 2")
print("if a password name is not found terminal will output ^7")
choice = input()
if choice == "1":
    print ("how many characters would you like your password to be?")
    length = int(input())
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symbols = "!@#$%^&*()?~"
    all = lower + upper + num + symbols
    temp = random.sample(all,length)
    password = "".join(temp)
    print ("your password is: " + password)
    print ("do you want to save your password? (y/n)")
    if input() == "y":
        print ("what would you like to name your password?")
        name = input()
        f = open("passwords.txt", "a")
        f.write(name + ": " + password + "\n")        
        f.close()
    print ("Your password has been saved to passwords.txt and will be kept forever unless you delete the file.")
    print ("ok, goodbye")
    exit()
elif choice == "2":
    print ("what is the name of your password?")
    name = input()
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(name + ":"):
                print ("your password is: " + line.split(": ")[1].strip())
                break
        else:
            print ("password not found")
    print ("ok, goodbye")
    exit()
else:
    print("Invalid input. Goodbye.")