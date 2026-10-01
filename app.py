# def oddoreven(input):
#     if input % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# oddoreven(67)


# tipoptions = [0, 15, 20, 25, 100]
# serviceoptions = ["bad", "okay", "good", "great", "phenomenal"]

# def tipfunction(bill, service):
#     tip = "nothing"
#     for i in serviceoptions:
#         if i == service:
#             tip = tipoptions[serviceoptions.index(i)]
#     if tip == "nothing":

#         while True:
#             service = input("What?")
#             breakloop = False
#             for i in serviceoptions:
#                 if i == service:
#                     tip = tipoptions[serviceoptions.index(i)]
#                     breakloop = True
#             if breakloop:
#                 break

    
#     print("paid amount:", bill)
#     print("service:", service)
#     print("tip:", tip, "%")
#     total = float(bill) + float(bill)*float(tip)*0.01
#     total = round(total, 2)

#     print("total:", total)


# bill = input("Input bill.")
# bill = float(bill)

# service = input("How was the service?")

# tipfunction(bill, service)





# list = []
# number = input("input number: ")
# number = int(number)
# def factors(insertednumber):
#     loopnum = insertednumber + 1
#     for i in range(loopnum):
#         if i != insertednumber:
#           subtractionresult = insertednumber - i
#           if insertednumber % subtractionresult == 0:
#              list.append(subtractionresult)
# factors(number)
# print("factors:")
# for i in list:
#     print(i)







#finding greatest common factor of two numbers

# input1 = input("input first number")
# input2 = input("input second number")
# def findgcf(number1, number2):
#     number = 0
#     if number1 > number2:
#         number = number2
#     else:
#         number = number1
#     while True:
#         if number1 % number == 0 and number2 % number == 0:
#             print("GCF is", number)
#             break
#         number -= 1
# findgcf(int(input1), int(input2))





# #whiteboard test prep

# def spaces(N, Y, T):
#     amt = 0
#     for i in range(N):
#         if Y[i] == T[i] and Y[i] == "C":
#             amt += 1
#     print(amt)
# spaces(5, ["C", ".", ".", "C", "C"], ["C", "C", "C", ".", "C"])





# # number guessing game

# import random
# guess_history = []
# number = random.randint(1, 10)
# while True:
#     guess = input("Guess the number!")
#     guess = int(guess)

#     def printwrong(table):
#         print("Already chosen numbers:")
#         for i in table:
#             print(i)

#     if int(guess) == number:
#         print("WINNER!")
#         printwrong(guess_history)
#         break
#     else:
#         if not guess in guess_history:
#             print("Wrong.")
#             guess_history.append(guess)
#         else:
#             print("That was an already guessed number")
#         if guess > number:
#             print("your guess is greater than the selected number")
#         else:
#             print("your guess is smaller than the selected number")
#     printwrong(guess_history)



# Answers:
# The name of an item CAPS SENSITIVE
# "yes"
# "no"
# "show me my cart"


items = [
    {
        "Name": "Couch",
        "Price": 499.99,
        "Description": "The comfiest couch you will ever sit on."
    },

    {
        "Name": "Chair",
        "Price": 49.99,
        "Description": "The perfect chair for your home."
    },

    {
        "Name": "Iphone 18 pro max",
        "Price": 1298.99,
        "Description": "500 new features from the last Iphone. And better camera quality."
    },

    {
        "Name": "Medieval Sword Prop",
        "Price": 35.99,
        "Description": "Doubles as furniture for your home, you don't have to be making a movie to buy this."
    }
]

cart = [

]

first = True
didnt_understand = False
while True:

    print("List of items:")
    for i, v in enumerate(items):
        print(i+1, ")", v["Name"])

    didnt_understandchanged = False

    answer = 0
    if didnt_understand:
        didnt_understand = False
        didnt_understandchanged = True
        answer = input("Could you repeat that?")
    elif first:
        answer = input("Would you like to purchase an item? If so, please say which one.")
    else:
        answer = input("Would you like to purchase another item? If so, please say which one.")

    if answer.lower() == "show me my cart":
        if len(cart) == 0:
            print("You have nothing in your cart.")
            continue
        
        for i, v in enumerate(cart):
            print(i+1, ")", v["Name"])
        continue

    item = False
    for i, v in enumerate(items):
        if v["Name"] == answer:
            item = v

    if not item:
        if answer.lower() == "no": # purchase

            if didnt_understandchanged:
                finalanswer = input("Do you want to leave?")
                if finalanswer.lower() != "yes":
                    continue

            if len(cart) == 0: # nothing in cart
                print("Okay, goodbye!")
                break
            
            total = 0
            print("Okay, here are the items you bought and the total.")
            for i, v in enumerate(cart):
                print(i+1, ")", v["Name"])
                total += v["Price"]
            print("Total:", total)
            break

        else: # something else said
            didnt_understand = True
            continue
    else: # item was said
        price = str(item["Price"])
        print(item["Name"] + ":", item["Description"], "$" + price)
        finalanswer = input("Are you sure you want to purchase this?")
        if finalanswer.lower() == "yes":
            print("The item has been added to your cart!")
            first = False
            cart.append(item)
            