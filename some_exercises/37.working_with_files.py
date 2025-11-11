# 1. S satr berilgan. Agar S faylning mumkin bo'lgan nomi bo'lsa, u holda shu nomdagi bo'sh fayl hosil
# qilinsin va TRUE chop qilinsin. Agar S nomdagi faylni yaratish mumkin bo'lmasa u holda FALSE chop qilinsin.

# s = 'kitobar.txt'
#
# result = True
# if s == '' or s in ['@', '#', '$', '%', '^', '*', '~']:
#     result = False
#     print(result)
#
# if result:
#     file = open(s, 'x')
#     file.close()
#     print(result)



# 2. Fayl nomi va N butun soni berilgan (N > 1). Berilgan nomdagi fayl hosil qilinsin va unga N ta birinchi
# musbat juft sonlari chop qilinsin (2, 4, ...).

# file_nomi = 'juft_sonlar.txt'
# N = 7
#
# file = open(file_nomi, 'x')
# file.close()
#
# i = 1
# juft_sonlar_soni = 0
# while True:
#     f = open(file_nomi, 'a')
#     if i%2==0:
#         f.write(str(f'{i} '))
#         juft_sonlar_soni+=1
#     i+=1
#     if juft_sonlar_soni == N:
#         break
#
# f.close()
#
# s = open(file_nomi, 'r')
# f2 = s.read()
#
# print(f2.split())



# 3. Fayl nomi va A va D haqiqiy sonlar berilgan. Shu nomdagi fayl hosil qilinsin va unga A boshlang'ich hadi va
# D farqiga ega bo'lgan arifmetik progressiyaning birinchi 10 ta hadi yozilsin. A, A+D, A+2*D, A+3*D, ....

#
# file_nomi = 'hadlar.txt'
# A = 9
# D = 22
#
# # Faylni yangidan yaratamiz
# f = open(file_nomi, 'w')
#
# # 10 ta birinchi hadni yozish
# for i in range(10):
#     f.write(str(A + i * D) + ', ')
#
# f.close()
#
# # Faylni o‘qish
# f2 = open(file_nomi, 'r')
# s = f2.read()
# f2.close()
#
# print(s)



# # 4. 4 ta faylning nomi berilgan. Shu fayllarning nechtasi joriy katalogda joylashgani aniqlansin.
import os
# s = os.path.exists('gg.txt')
# file_nomlari = ['gg.txt', 'lia.txt', 'tech.txt', 'toq.txt']
# bor_filelar_soni = 0
# for i in file_nomlari:
#     if os.path.exists(i):
#         bor_filelar_soni += 1
# print(bor_filelar_soni)



# # File5. Butun sonlar fayli berilgan. Shu fayl tarkibiga kiruvchi elementlar soni aniqlansin. Agar bunday fayl
# # mavjud bo'lmasa u holda -1 chop qilinsin.
#
#
# if os.path.exists('gg.txt'):
#     file = open('gg.txt', 'r')
#     f = file.read()
#     print(len(f.split()))
#     file.close()
# else:
#     print(-1)




# # 6. Manfiy bo'lmagan butun sonlardan iborat fayl va K soni berilgan (K butun). Faylning K - elementi chop qilinsin
# # (elementlar 1 dan boshlab nomerlanadi). Agar bunday element mavjud bo'lmasa, (-1) chop qilinsin.
#
# file_nomi = 'gg.txt'
# K = 8
#
# file = open(file_nomi, 'r')
# f = file.read()
# if len(f.split()) >= K:
#     for i in f.split():
#         if K == 1:
#             print(i)
#         K-=1
# else:
#     print(-1)




# 7.

# file = open('gg.txt', 'r')
# s = file.read()
# print(s.split()[0])
# print(s.split()[1])
# print(s.split()[-1])
# print(s.split()[-2])
# file.close()



# 8.

file = open('gg.txt', 'r')