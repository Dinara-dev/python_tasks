# 1. Input orqali son kiriting tugagan sonigacha key ni valuesida shu formula asosida ishlasin (x, x * x)
# Kutilayotgan natija: {1:1, 2:4, 3:9, 4:16, 5:25}
#
# n=int(input("Enter any numbers:"))
#
# solo = {k: k*k for k in range(1, n+1) }
# print(solo)

#
# 2. Lug'atdagi barcha qiymatlarni yig'ish va arifmetik o'rtachani chiqarish uchun Python dasturini yozing.
#
# n = int(input("Enter any numbers:"))
#
# solo = {k: k*k for k in range(1, n+1)}
# values = solo.values()
# total = sum(values)
# average = total / len(values)
#
# print("Dictionary:", solo)
# print("Yig‘indisi:", total)
# print("O'rtacha:", average)
#
# 3.Ikki roʻyxatni kalit: qiymat lugʻatiga birlashtirish uchun Python dasturini yozing. RO'YXATLAR BIR HAJIMDA bo'lishi kerak [key] [values] {key, value}
# [a b c] [d g f]   {a:d, b:g, c:f}
#
# l1 = ['a', 'b', 'c']
# l2 = ['d', 'g', 'f']
#
# d = dict(zip(l1, l2))
# s = ','.join(f'{k}:{v}' for k, v in d.items())
# print(f'{{{s}}}')

#
# 4. Shaharlar koordinatalari lug'ati mavjud.
#
# cities = {
#     'Moscow': [550, 370],
#     'London': [510, 510],
#     'Paris': [480, 480],
# }
#
#Quydagi formuladan foydalanib, ular orasidagi masofalarning lug'atlarini tuzing:
# ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#
# distances = {}
#
# moscow = cities['Moscow']
# london = cities['London']
# paris = cities['Paris']
#---------------------------------------------------------------------------------------------------------------

# cities = {
#     'Moscow': [550, 370],
#     'London': [510, 510],
#     'Paris': [480, 480],
# }
#
# distances = {}
# for city1, coord1 in cities.items():
#     for city2, coord2 in cities.items():
#         if city1 < city2:
#             x1, y1 = coord1
#             x2,y2 = coord2
#             distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
#             distances[(city1, city2)] = distance
#
# for (city1, city2), distance in distances.items():
#  print(f'{city1} → {city2}: {distance:.2f}')


#----------------------------------------------------------------------------------------------------
# 5. **. Mahsulot kodlari lug'ati va stokdagi tovarlar miqdori lug'ati mavjud.
# Har bir mahsulot toifasining umumiy narxini ko'rsating

goods = {
    'Lampa': '12345',
    'Stol': '23456',
    'Divan': '34567',
    'Stul': '45678',
}

store = {
    '12345': [
        {
            'quantity': 27,
            'price': 42
        },
    ],
    '23456': [
        {
            'quantity': 22,
            'price': 510
        },
        {
            'quantity': 32,
            'price': 520
        },
    ],
    '34567': [
        {
            'quantity': 2,
            'price': 1200
        },
        {
            'quantity': 1,
            'price': 1150
        },
    ],
    '45678': [
        {
            'quantity': 50,
            'price': 100
        },
        {
            'quantity': 12,
            'price': 95
        },
        {
            'quantity': 43,
            'price': 97
        },
    ],
}

# 6. Ikki lug'atni uchinchi lug'atga birlashtirish   {dic1} {dict2} {dict3} **