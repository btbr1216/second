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



# input1 = input("input first number")
# input2 = input("input second number")
# def findgcf(number1, number2):
#     number = 1
#     while True:
#         if number % number1 == 0 and number % number2 == 0:
#             print("GCF is", number)
#             break
#         number += 1
# findgcf(int(input1), int(input2))



import random
number = random.randint(1, 10)
guess = input("Guess the number!")
if int(guess) == number:
    print("WINNER!")