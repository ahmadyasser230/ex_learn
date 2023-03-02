# # first_name = "Ahmad"
# # last_name = "Mohaisen"
# # age = 21
# # height = 175
# # address = "Gaza-palestain"
# # print (f""" {first_name}
# # {last_name}
# # {age}
# # {height}
# # {address}""")
# # weight = input("please enter your weight")
# # size =  float(weight) /.45
# # print(f"{size} bound")
# #
# #
# # from math import floor
# # x = 3.5
# # y = math.floor(x)
# # print(y)
# #
# #
# # import decimal
# # import math
# # x = 0.1
# # y = 0.2
# # z = 0.3
# # i = x + y - z
# # print(decimal.Decimal(i))
# # print(decimal.Decimal(0.0))
# # print(math.isclose(i , 0.0))
# #
# #
# # number = input("Enter Your Number: ")
# # digits = number.split()
# # result = ""
# # for one_digit in digits:
# #     result = result + str(int(one_digit)**2)
# # print(result)
# #
# #
# # course = "aws restart program"
# # # firset_char = course[5:-1]
# # course[0:4] = "code"
# # print(course)
# #
# #
# # weather = input("enter the weather hot or cold")
# # if weather == "it is hot":
# #     print("it is a hot day \n Drink plenty of water")
# # elif weather == "it is cold":
# #     print("it is a cold day \n Wear warm clothes")
# # else:
# #     print(" It's a lovely day")


# print("whate you have")
# bank = int(input(" 1-high_income or good_credit \n 2-high_income and good_credit"))
# high_income = 1
# good_credit = 2
# togather = high_income and good_credit
# togather = 2
# choose = high_income or good_credit
# choose = 1
# if bank == 2:
#     print("Allow")
# elif bank == 1 :
#     print("half Allow")
# else:
#     print("Not Allow")

# print("Enter your name")
# name = input()
# if len(name) < 3:
#     print("short name")
# elif len(name) > 10:
#     print("long name")
# else:
#     print("good name")

# print("enter your avreage")
# avg = float(input())
# if avg >= 90:
#     print("A")
# elif avg >= 80:
#     print("B")
# elif avg >= 70:
#     print("c")
# elif avg >= 60:
#     print("D")
# else:
#     print("أبوك جايبلك هدية")

# i=1
# con_weight = 0
# while i <= 2:
#     print("what the your weight")
#     weight = float(input())
#     print("kg or ibs")
#     size = input()
#     if size == "kg":
#         con_weight = f"{weight / 0.45} ibs"
#         break
#     elif size == "ibs":
#         con_weight = f"{weight * 0.45} kg"
#         break
#     i+=1
# else:
#     print("error")
# print(con_weight)



# i = 0
# while i < 6:
#     i += 1
#     if i == 4:
#         continue
#     print(i)
# print("Done")



# secret_num = 3
# i = 1
# while i <=3:
#     print("Enter the number guess between1 to 9")
#     num = int(input())
#
#     if num == secret_num :
#         print("you won")
#         break
#     i+=1
# else:
#     print("sorry you failed")

# list_of_numbers = [10,3,5,76,324,-4234,656]
# max=0
# min=0
# for x in list_of_numbers:
#    if x > max :
#       max = x
#    else :
#       min = x
# print(max)
# print(min)

# start=True
# stop=False
# print("inter the state of car")
# car =int(input("1-start \n 2-stop \n 3-quit \n 4-help"))
# if car== 1:
#     if start == True:
#         print("car is already started if the car is started")
#     else :
#         print(" car started")
# elif car == 2:
#     if stop == False:
#         print("car stopped eif does not stop")
#     else:
#         print("car already stopped if it is running")
# elif car == 3 :
#     exec
#
# elif car == 4 :
#     print("start - to start the car \n  stop - to stop the car \n quit - to quit ")




# state = True
# action = ""
# while action != "quit":
#     action= input("enter")
#     if action == "start":
#         if state == True:
#             print("car already started")
#         else:
#             print("car is starting")
#             state= True
#     elif action == "stop":
#         if state == True:
#             print("cat stopped eif does not stop")
#             state = False
#         else:
#             print("car already stopped if it is running")
#     elif action == "help":
#         print("start - to start the car \n  stop - to stop the car \n quit - to quit ")
# else:
#     exit
# emojes = {
#     "happy" : "😊",
#     "sad" : "😢"
# }
# result = input("Do you happy")
# list_of_words = result.split(" ")
# for word in list_of_words:
#     print(emojes.get(word,word))

# num = {
#     "0":"zero",
#     "1":"one",
#     "2":"tow",
#     "3":"three",
#     "4":"four",
#     "5":"faive",
#     "6":"six",
#     "7":"saven",
#     "8":"eghit",
#     "9":"nine"
# }
# resalt = input("write three number from 0 to 9")
# list = resalt.split(" ")
# res = ""
# for number in list:
#     res+=num.get(number, number)
# print(res)



# def emoje():
#     emojes = {
#         "happy": "😍",
#         "sad": "😢"
#     }
#     result = input("what you filing")
#     list = result.split(" ")
#     res=""
#     for word in list:
#         res+=emojes.get(word, word)
#     print(res)
#
# emoje()



# def limits_test(limit ,add_value ,*numbers):
#     result=0
#     for i in numbers:
#         if i > limit:
#             print(i,"old value")
#         else:
#             result=i+add_value
#             print(result)
# limits_test (5, 3 ,4)

# num = {
#     "0":"zero",
#     "1":"one",
#     "2":"tow",
#     "3":"three",
#     "4":"four",
#     "5":"five",
#     "6":"six",
#     "7":"seven",
#     "8":"eight",
#     "9":"nine"
# }
# resalt = input("write three number from 0 to 9")
# list = resalt.split(" ")
# res = ""
# for number in list:
#     res+=num.get(number, number)
# print(res)


# def int_to_roman(number):
#     number=int(input("Enter number from 1 to 15"))
#     if number == 1:
#         print("I")
#     elif number == 2:
#         print("II")
#     elif number == 3:
#         print("III")
#     elif number == 4:
#         print("IV")
#     elif number == 5:
#         print("V")
#     elif number == 6:
#         print("VI")
#     elif number == 7:
#         print("VII")
#     elif number == 8:
#         print("VIII")
#     elif number == 9:
#         print("IX")
#     elif number == 10:
#         print("X")
#     elif number == 11:
#         print("XI")
#     elif number == 12:
#         print("XII")
#     elif number == 13:
#         print("XIII")
#     elif number == 14:
#         print("XIV")
#     elif number == 15:
#         print("XV")
#     else:
#         print("Number out of range")
# int_to_roman(1)


#
# def convert_to_roman():
#     num = int(input("Enter number"))
#     if num < 1 or num > 1000:
#        print( "Number out of range!")
#     else:
#         con = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
#         rom = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
#         result = ""
#         for i in range(0, len(con)):
#             while num >= con[i]:
#                 num =num - con[i]
#                 result =result + rom[i]
#         print(result)
# convert_to_roman()



# def contain_7(*number):
#   res = input("enter list of number contain 7 numbers")
#   list = res.split(",")
#   for num in number:
#         list.append(num)
#   for i in list:
#       if i== 0:
#           d = list.index(i)
#           if list[d+1]==0 and list[d+2] == 7 :
#               print( True)
#       else:
#           print (False)
# contain_7()

# def pattern_finder(*numbers):
#     num_list = []
#     for num in numbers:
#         num_list.append(num)
#     for numb in num_list:
#         if numb == 0:
#             ind = num_list.index(numb)
#             if num_list[ind+1] == 0 and num_list[ind+2] == 7:
#                 print(True)
#                 return True
#             else:
#                 print(False)
#                 return False
#
# pattern_finder(1,2,3,4,0,7,1,0,0,7)




