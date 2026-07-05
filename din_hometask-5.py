# 1.Uchta sondan maksimal sonni topadigan funksiyani yozing.
#
# def nums(a, b, c):
#     max_value = a
#     if b > max_value: max_value = b
#     if c > max_value: max_value = c
#     return max_value
#
# print(nums(5,6,3))

# -----------------------------------------------------------------------------------------------------------
# 2.Ro’yxatdagi hamma sonlarni yig’indisini chiqaradigan funksiyani yarating.pythonga o’rnatilgan sum funksiyadan foydalanmang.
# Roʻyxat namunasi: [8, 2, 3, 0, 7] +=
# Kutilayotgan natija: 20
#
# numbers = [8, 2, 3, 0, 7]
# def yigindi(numbers):
#     total = 0
#     for  num in numbers:
#         total +=num
#     return total
# print(yigindi(numbers))
#
# 3.Ro’yxatdagi hamma sonlarni ko’paytmasini chiqaradigan funksiya yarating.
# Roʻyxat namunasi: [8, 2, 3, -1, 7]
# Kutilayotgan natija: -336
#
# numbers = [8, 2, 3, -1, 7]
# def kopaytma(numbers):
#     total = 1
#     for num in numbers:
#         total *= num
#     return total
# print(kopaytma(numbers))

# 4.Matnni teskari tartibga o’zgartiradigan funksiya yozing:
# matn namunasi: 1234abcd
# kutilayotgan natija: dcba4321

# def teskari (text):
#     teskari_text = text[::-1]
#     return teskari_text
# print(teskari(' 1234abcd'))

#
# 5.Matn qabul qiladigan funksiya yarating va bosh, kichik harflar sonini hisoblaydigan funksiya yozing. .islower(), .isupper()
#
# Matn namunasi: 'The quick Brow Fox'
# Kutilayotgan natija:
# Bosh harflar soni: 3
# Kichik harflar soni: 12

# def harflar(text):
#     upper = 0
#     lower = 0
#     for  i in text:
#         if i.isupper():
#             upper += 1
#         elif i.islower():
#             lower += 1
#     print ('Bosh harflar soni:', upper)
#     print ('Kichik harflar soni:', lower)
#
# harflar('The quick Brow Fox')
#
# 6.Palindrom so’zlar.
# So’z qabul qiladigan funksiya yozing va u palindrom ekanligini aniqlaydigan funksiya yozing.
# True - Анна, казак, нон
#
# def palindrom (word):
#     word = word.lower()
#     if word == word[::-1]:
#         return True
#     else:
#         return False
# text = input('Enter a word: ')
# print(palindrom(text))

#
# 7.Foydalanuvchi bankka omonat qo’yyapti ‘x’ rubl miqdorida ‘y’ yil mobayniga 10 % yilliga.
# Bank funksiyasini yozing u pul va yil miqdorini qabul qilsin foydalanuvchidan va y yildan keyin bo’ladigan pul miqdorini qaytarsin.
#
# def omonat(x, y):
#     for i in range(y):
#         x *=1.10
#     return x
# print(omonat(2000, 5))

#
# 8.Funksiya orqali ro’yxatdan 15 ga bo’linadigan sonlarni chiqaring.
# nums = [45, 55, 60, 37, 100, 105, 220]

# nums = [45, 55, 60, 37, 100, 105, 220]
# def bolinadigan(nums):
#     result = []
#     for num in nums:
#         if num % 3 == 0 and num % 5 == 0: result.append(num)
#     return result
# print(bolinadigan(nums))


# 9.(qo'shimcha vazifa) Undan oldin bo’lgan hamma uy vazifalarini funksiya orqali bajarib ko’ring.

# 2.7 **. Shokoladka to’g’ri to’rtburchak shaklga ega va kengligi x uzunligi bolgan to’rtburchak shakllarga bo’lingan.
# Shokoladni bir martta to’g’ri chiziq bo’yicha ikki qismga sindirsa bo’ladi.
# Aynan x bo’lakdan iborat shokolad bo’lagini shu tarzda sindirish mumkinligini aniglang.
# Dastur kirish sifatida uchta sonni qabul qiladi: kenglik, uzunlik, qismlar va YES yoki NO yozuvini konsolga chiqarish kerак.

# def shokolad (k,u,x):
#     if x % k == 0 or x % u == 0:
#         return'Yes'
#     else:
#         return 'No'
# print(shokolad(4,5,8))