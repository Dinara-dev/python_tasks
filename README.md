# python_tasks
# 1. Foydalanuvchi ismini so’raydigan va unga salom beradigan dastur yozing.

# name = input('Ismingizni kiriting:')
# print( f'Salom! {name}')

# 2. Foydalanuvchidan 3 ta son so’raydigan va ularning yig’indisini chop etadigan dastur yozing.

# num1 = int(input('Istalgan 1ta son kiriting:'))
# num2 = int(input('Istalgan 2chi son kiriting:'))
# num3 = int(input('Istalgan 3chi son kiriting:'))
#
# summa = num1 + num2 + num3
# print('uchta sonning yigindisi:', summa)

# 3. 6 ta maktab o’quvchilari 50 ta olmani teng taqsimlashdi. Bo’linmaydigan qoldiq savatda qoldi.
# Har bir o’quvchi nechta olma oladi? Savatda nechta olma qoladi? Istalgan miqdordagi o’quvchilar va olmalar uchun topshiriqni bajaring.

# print(50%6)
# print(50//6)
#
# students = int(input("O‘quvchilar soni: "))
# apples = int(input("Olmalar soni: "))
#
# each = apples // students
# remainder = apples % students
#
# print("Har bir o‘quvchi oladi:", each)
# print("Savatda qoladi:", remainder)


# 4. Foydalanuvchidan raqam so'raydigan va shu raqamdan oldingi va keyingi sonni chop etadigan dastur yozing:
# Misol
# Raqamni kiriting: 1345
# Keyingi raqam: 1346
# Oldingi raqam: 1344

# num = int(input('Istalgan son kiriting:'))
#
# print(num)
# print(f'Oldingi son: {num-1}')
# print(f'Keyingi son: {num+1}')

# 5. Matnni biriktirilgan fayldagi kabi formatda chiqaradigan dastur tuzing.

# print(f'Twinkle, twinkle, little star,\n'
#    f' How I wonder what you are!\n'
#     f'   Up above the world so high,\n'
#     f'    Like a diamond in the sky.\n'
# f'Twinkle, twinkle, little star,\n'
#     f'How I wonder what you are\n')

# 6. Quyidagi uchta o'zgaruvchini kutilgan natijaga ko'ra formatlash usulini qo'llash dasturini yozing.
#
# Pul = 1200
# Soni = 3
# Narxi = 400
#
# Kutilayotgan natija:
# Menda 1200 dollar bor, shuning uchun 400 dollarga 3 ta futbol to'pini sotib oldim.

amount = int(input('Istalgan pul miqdorini kiriting:'))
num = int(input('Futbol topi sonini kiriting:'))
price= int(input('Futbol topi narxini kiriting:'))


print(f'Menda {amount}dollar bor, shuning uchun {price} dollarga {num}ta futbol topini sotib oldim.')
