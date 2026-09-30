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






items = [
    {
        "Name": "Couch",
        "Price": "499.99",
        "Description": "The comfiest couch you will ever sit on."
    },

    {
        "Name": "Chair",
        "Price": "49.99",
        "Description": "The perfect chair for your home."
    },

    {
        "Name": "Iphone 18 pro max",
        "Price": "1298.99",
        "Description": "500 new features from the last Iphone. And better camera quality."
    },

    {
        "Name": "Medieval Sword Prop",
        "Price": "35.99",
        "Description": "Doubles as furniture for your home, you don't have to be making a movie to buy this."
    }
]

#

first = True
didnt_understand = False
while True:
    print("List of items:")
    for i, v in enumerate(items):
        print(i+1, ")", v["Name"])
    answer = 0
    if first:
        first = False
        answer = input("Would you like to purchase an item? If so, please say which one.")
    elif didnt_understand:
        didnt_understand = False
        answer = input("Could you repeat that?")
    else:
        answer = input("Would you like to purchase another item? If so, please say which one.")
    item = False
    for i, v in enumerate(items):
        if v["Name"] == answer:
            item = v
    if not item:
        didnt_understand = True
        continue