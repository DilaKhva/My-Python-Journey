# # 15
#
# K = 6
# file_nomi = 'lia.txt'
#
# file = open(file_nomi, 'r')
# s = file.readlines()
# # matn_listi = s.split()
# file.close()
# # print(s)
# if K <= len(s):
#     s.pop(K-1)
#
#     file2 = open(file_nomi, 'w')
#     s2 = file2.writelines(s)
#     file2.close()
# # print(s)
# else:
#     pass
from dataclasses import replace

# # 16.
#
# file_nomi = 'lia.txt'
#
# file = open(file_nomi, 'r')
# s = file.readlines()
# print(s)
# for line in s:
#     print(line)
#     i = s.index(line)
#     # s.pop(i)
#     print(i)
#     if line == '\n':
#         s.pop(i)
# print(s)
# file.close()
#
# file2 = open(file_nomi, 'w')
# s2 = file2.writelines(s)
# print(s2)
# file2.close()



# # 17.
#
# file1_nomi = 'gg.txt'
# file2_nomi = 'lia.txt'
#
# file1 = open(file1_nomi, 'r')
# f1 = file1.readlines()
# file2 = open(file2_nomi, 'r')
# f2 = file2.readlines()
#
# print(f1)
# print(f2)
#
# file1.close()
# file2.close()
#
# for line in f1:
#     i = f1.index(line)
#     print(i)
#     for line2 in f2:
#         i2 = f2.index(line2)
#         print(i2)
#         if i == i2:
#             print('condition worked!')
#             inx += 1
#             f1.insert(i2+1, line2)
#         print('hi')
#
# print(f1)



# # 18.
#
# K = 7
# file_nomi = 'lia.txt'
#
# file = open(file_nomi, 'r')
# f = file.readlines()
# print(f)
# file.close()
#
# if len(f) > K:
#
#     for line in f:
#         i = f.index(line)
#         f.pop(i)
#         f.append(line[K:])
#         # print(line[K-1:])
# print(f)




# 19.

# file_nomi = 'lia.txt'




# file = open(file_nomi, 'r')
# f = file.read()
# file.close()
# print(f)
# file2 = open(file_nomi, 'w')
# for i in f:
#     if i != i.upper():
#         i = i.upper()
#         file2.write(i)
#     else:
#         i = i.lower()
#         file2.write(i)
#     print(i)
#
# file = open(file_nomi, 'r')
# f = file.read()
# print(f)
# file2.close()
# file.close()



# # 20
# file_nomi = 'lia.txt'
#
# file = open(file_nomi, 'r')
# f = file.read()
# print(f)
# file.close()
#
# # print(f.replace('  ', ' '))
#
# while '  ' in f:
#     f = f.replace('  ', ' ')
# print(f)
# file2 = open(file_nomi, 'w')
# f2 = file2.write(f)
# file2.close()



# #21
#
# file_nomi = 'lia.txt'
#
# file = open(file_nomi, 'r')
# f = file.readlines()
# print(f)
#
# if len(f) >= 3:
#     for j in range(-3, 0):
#         print(j)
#         print(f[j])
#         i = f.index(f[j])
#         f.pop(i)
#     print(f)
#     file.close()
#
#     file2 = open(file_nomi, 'w')
#     file2.writelines(f)
#     file2.close()
# else:
#     pass



# # 22
#
# K = 4
# file_nomi = 'lia.txt'
#
# file = open(file_nomi, 'r')
# f = file.readlines()
# file.close()
# file2 = open(file_nomi, 'w')
# if 10 > K > 0 and len(f) > K:
#     for i in range(-K, 0):
#         f.pop(i)
#     file2.writelines(f)
#
#     file2.close()
# else:
#     pass




# # 23
#
# K = 5
# file_nomi = 'lia.txt'
# file = open(file_nomi, 'r')
# f = file.readlines()
# file.close()
# if 0 < K < 10 and K < len(f):
#     for i in range(-K, 0):
#         print(f[i])
#         file2 = open('lia2.txt', 'a')
#         file2.writelines(f[i])
#         file2.close()
# else:
#     pass



# # 24
#
# file_nomi = 'lia2.txt'
#
# file = open(file_nomi, 'r')
# f = file.readlines()
# print(f)
# file.close()
# counter = 0
# for line in f:
#     if line != "\n":
#         counter += 1
# print(counter)



# # 25
#
# K = 4
# file_nomi = 'lia2.txt'
#
# file = open(file_nomi, 'r')
# f = file.readlines()
# file.close()
#
# if f[K] in f and f[K] != '\n':
#     print(f[K])
#     f.pop(K)
#     file2 = open(file_nomi, 'w')
#     file2.writelines(f)
#     file2.close()
# else:
#     pass



# 26
#
# file_nomi = 'lia2.txt'
#
# file = open(file_nomi, 'r')
# f = file.readlines()
# # print(f)
# file.close()
# count = 0
# for line in f:
#     # print(line)
#     if '     ' in line:
#         count += 1
#
# print(count)



# 44

with open('gg.txt', 'r') as f:
    a = f.readlines()
counter = 0
yigindi = 0
for i in a:
    # print(i)
    # print(i.strip())
    counter += 1
    yigindi = yigindi + int(i)
print('Miqdori:', counter)
print("Yigindisi:", yigindi)

