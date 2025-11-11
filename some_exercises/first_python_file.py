# name = str(input("What's your name? "))
# print("Nice to meet you,", name)
#
# age = int(input('How old are you? '))
#
#
# print(str(age)+"?", "Me too!")


# print(type("5"))
# print(type(5))
# print(type(5.0))


# 1. Write code to find the result of:

# print(15 // 4)
#
# print(15 % 4)
#
# print(2 ** 5)

#Write code that asks for a number and tells if it’s even or odd.

# son = int(input('Xoxlagan soningizni kiriting: '))
#
# if son % 2 == 0:
#     print("Siz juft son kiritdingiz.")
# else:
#     print("Siz toq son kiritdingiz.")


# yosh = int(input('Yoshingizni kiriting:'))
# if yosh >= 18:
#     print("Siz balog'at yoshidasiz")
# else:
#     print("Siz hali detskiysiz!")


# grade = int(input('Bahoni kiriting (1-5): '))
#
# if grade == 5:
#     print('Barakalla!')
# elif grade == 4:
#     print('Yaxshi!')
# elif grade == 3:
#     print('Qoniqarli.')
# else:
#     print("Yana urinib ko'ring.")



# Write a program that asks for your score (0–100) and prints:
#
# "Excellent" if score ≥ 90
#
# "Good" if 70 ≤ score < 90
#
# "Pass" if 50 ≤ score < 70
#
# "Fail" if score < 50
#

# your_score = int(input('What is your score? (0-100) '))
# if your_score >= 90:
#     print('Excellent')
# elif 70 <= your_score < 90:
#     print('Good')
# elif 50 <= your_score < 70:
#     print('Pass')
# else:
#     print('Fail')

# Write a program that asks for a number and prints:
#
# "Positive" if it’s > 0
#
# "Negative" if it’s < 0
#
# "Zero" if it’s 0


# num = int(input('Xoxlagan soningizni kiriting: '))
#
# if num > 0:
#     print('Positive')
# elif num < 0:
#     print('Negative')
# else:
#     print('Zero')



# 💬 Mini tasks for you:
#
# Write a program that asks for a number and checks if it’s between 10 and 20 (inclusive).
# → Print "Yes, it’s between 10 and 20" or "No, it’s not"
#

# son = int(input("Ma'lum bir son kiriting: "))
# if son < 20 and son > 10:
#     print("Yes, it's between 10 and 20")
# else:
#     print("No, it's not.")

# Write a program that asks for a day and checks if it’s a weekend (Saturday or Sunday).
# → Print "Weekend!" or "Weekday."


# kun = str(input("Bugun qaysi kun? "))
# if kun == 'Dushanba' or kun == 'Seshanba' or kun == 'Chorshanba' or kun == 'Payshanba' or kun == 'Juma':
#     print("Weekday.")
# elif kun == 'Shanba' or kun == 'Yakshanba':
#     print('Weekend')
#
#
# while True:
#     print("Forever looping!")


# while True:
#     word = input("Type 'stop' to end: ")
#     if word == 'stop':
#         break

#
# Write a for loop that prints numbers from 1 to 10.
#
# for i in range(10):
#     print(i+1)


# Write a while loop that does the same thing.
#
# while True:
#     print('Hello World!')


# Write a for loop that prints only even numbers from 2 to 20.

# for i in range (2, 20):
#     if i % 2 == 0:
#         print(i)

#
# counts = 1
# while counts <= 10:
#     print(counts)
#     counts +=1
#
#
#
# games = ['mlbb', 'cs2', 'genshin']
# for game in games:
#     print(game)


# numbers = [3, 2, 9, 51, 0, 62, 44, 1, 89]
#
# numbers.append(27)
#
#
#
# numbers.remove(0)
# print(len(numbers))


# full_name = "Dilnoza Kholisova"
#
# print(full_name[:7])
# print(full_name[8:])

# my_word = " Python is fun! "
# my_word = my_word.strip()
# my_word = my_word.upper()
# my_word = my_word.replace("FUN", "awesome")
# print(my_word)

# word = 'assalomu alaykum'
# changed_word = ''
# for i in word.split():
#     first = i[0]
#     for j in i:
#         if j == first:
#
#
#



# a = 'sdsferw wfwef ihdfhui woeufh'
# b = []
# for item in a.split():
#     s = item[0]
#     x = item[1:].replace(s, '.')
#     b.append(s+x)
# print(''.join(b))


# a = 'sdsferw wfwef ihdfhui woeufh'
# b = []
# for item in a.split():
#     s = item[-1]
#     x = item[:-1].replace(s, '.')
#     b.append(x+s)
# print(''.join(b))


# file = open('gg.txt', 'r')   #file nomi kengaytmasi bilan # file but in python module
# # s = file.read()
# s1 = file.readlines()
# print(s1)
# file.close()


# file = open('first_python_file.py', 'r')
# print(file.read())
# file.close()


# file = open('gg.txt', 'r')
# f = file.read()
# print(f)
# file.close()


# f = open('gg.txt', 'r')
# file = f.read()
# print(file)
# f.close()


# file = open('toq.txt', 'x')
# file.write('')
#
# file.close()


# file = open('lia.txt', 'a')
# file.write('Hello world')
#
# file.close()

# file = open('lia.txt', 'w')
# file.write('Hello world')
#
# file.close()


# file = open('lia.txt', 'a')
# for i in range(5):
#     file.write('Hello world gg\n')
#
# file.close()


# file = open('lia.txt', 'r')
# s = file.read()
# # print(s[::-1])
# file.close()
#
# file2=open('gg.txt', 'w')
# file2.write(s[::-1])
# file2.close()

# file = open('lia.txt', 'r')
# s = file.read()
# file.close()
#
# f2 = open('juft.txt', 'a')
# f3 = open('toq.txt', 'a')
# for i in s.split():
#     if int(i)%2==0:
#         f2.write(f'{i} ')
#     else:
#         f3.write(f'{i} ')
# f2.close()
#


# file = open('lia.txt', 'r')
# s = file.read()
# print(s)
# file.close()
#
# a = list(map(int, s.split()))
# print(a)
# # for i in range(1, len(a)-1):



