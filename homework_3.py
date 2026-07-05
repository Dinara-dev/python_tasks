# DINARA
# 1. a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] roʻyxati mavjud.
#
# Agar son 5 dan kichik yoki teng bo’lsa alohida ro’yxatga chiqaring va son 5 dan katta bo’lsa alohida ro’yxatga chiqaring.
# Misol
# Beshdan kichik yoki teng: [1, 1, 2, 3, 5]
# Beshdan katta: [8, 13, 21, 34, 55, 89]

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# kichik_yoki_teng = []
# katta = []
#
# for son in a:
#     if son <= 5:
#         kichik_yoki_teng.append(son)
#     else:
#         katta.append(son)
#
# print("Beshdan kichik yoki teng:", kichik_yoki_teng)
# print("Beshdan katta:", katta)

#------------------------------------------------------------------------------------------------------------

# 2. Siz foydalanuvchidan uning ismi, familiyasi, yoshini qabul qilasiz.
# Ularni tegishli o'zgaruvchilarga saqlang. Olingan qiymatlarni ro'yxatga saqlang.

# ism = input("Ismingizni kiriting:")
# familiya = input("Familiyangizni kiriting:")
# yosh = int(input("Yoshingizni kiriting:"))
#
# proweb_student = [ism, familiya, yosh]
# print("Ro'yxat:", proweb_student)
#
#----------------------------------------------------------------------------------------------------------------------------
# 3. Foydalanuvchidan vergul va boshliq bilan ajratilgan sonlar ketma ketligini qabul qiladigan dasturni yozing.
# Keyin esa har bir sonni ro’yxat va kortejga joylashtiring.

# Misol
# Sonlarni kiriting: 2, 3, 4, 5, 123, 3, 4, 5, 5678, 3, 4, 53, 2
# Ro’yxat: [‘2’, ‘3’, ‘4’, ‘5’, ‘123’, ‘3’, ‘4’, ‘5’, ‘5678’, ‘3’, ‘4’, ‘53’, ‘2’].
# Kortej: (‘2’, ‘3’, ‘4’, ‘5’, ‘123’, ‘3’, ‘4’, ‘5’, ‘5678’, ‘3’, ‘4’, ‘53’, ‘2’)
#
# a = input("Probeldan keyin sonlarni kiriting: ")
# sonlar = a.split(", ")
# royxat = list(sonlar)
# kortej = tuple(sonlar)
#
# print("Ro’yxat:", royxat)
# print("Kortej:", kortej)


#----------------------------------------------------------------------------------------------------------------------------
# 4. Foydalanuvchidan sonlarni qo’shish misolini qabul qiladigan
# (sonlar + orqali ajratilgan bo’lishi lozim) va yig’indini qaytaradigan dasturni yozing.
# Misol
# Qo’shishga doir misol kiriting: 3 + 5 + 5  +=
# 13
#
# sonlar = input(" Qo'shishga doir misol kiriting (masalan: 3 + 5 + 5): ")
#
# sonlar = sonlar.replace(" ", "")
# sonlar_list = sonlar.split("+")
# yigindi = 0
# for son in sonlar_list:
#     yigindi += int(son)
# print("Yig'indi:", yigindi)

#------------------------------------------------------------------------------------------------------------
# 5. Foydalanuvchidan uchta ismni qabul qiladigan bitta input() funksiyada dasturni yozing.
# Foydalanuvchidan uchta ismni terishini so’rang bo'shliq orqali ajratilgan.
# Kiritilgan matnni bo'shliq bo’yicha ajrating split() metod orqali uchta alohida ism bo’lishi uchun

# ismlar = input("Uchta ismni kiriting (bo'shliq bilan ajratilgan): ")
# ism_list = ismlar.split(" ")
# print("Ismlar ro'yxati:", ism_list)

#------------------------------------------------------------------------------------------------------------
#
# 6. Sonlar ro’yxati berilgan har bir sonni kvadrat darajaga ko’taradigan dastur yozing.
# Berilgan:
# numbers = [1, 2, 3, 4, 5, 6, 7]
# kutiladigan natija:
# [1, 4, 9, 16, 25, 36, 49]

numbers = [1, 2, 3, 4, 5, 6, 7]
kvadratlar = []

for i in numbers:
    kvadratlar.append(i**2)

print('sonlar:', numbers)
print('kvadratlari:', kvadratlar)



