# Dars 2. Uy vazifasi
# Daraja: asosiy
#
# 1.Dastur foydalanuvchining yoshini so'raydi.
# Agar yosh 18 dan kichik yoki unga teng bo'lsa, unda chop eting: "Siz o'qishingiz kerak."
# Agar yosh 18 dan katta, lekin 50 dan kichik yoki teng bo'lsa - "Siz ishlashingiz kerak"
# Agar yosh 50 dan katta bo'lsa, lekin 59 dan kam yoki unga teng bo'lsa - "Siz yaqinda nafaqaga chiqasiz"
# Agar yosh 59 dan katta, lekin 110 dan kam bo'lsa - "Siz nafaqaxo'rsiz."
# Agar foydalanuvchi haqiqiy bo'lmagan yoshga kirsa, nima ko'rsatilishi kerakligini ham ko'rib chiqing. Masalan, 1200.
#

# yosh =int(input("Yoshingizni kiriting:"))
# if yosh <=18: print("Siz o'qish yoshidasiz.")
# elif yosh >=18 and yosh <=50: print("Siz ish yoshidasiz")
# elif yosh >50 and yosh <=59: print("Siz yaqinda nafaqaga chiqasiz")
# elif yosh >59 and yosh <110: print("Siz nafaqa yoshidasiz")
# else: print("Ma'lumot mavjud emas!")
#---------------------------------------------------------------------------------------------------------------------------------------------

# 2.3 ta raqamni so‘raydigan va ularni qo‘shuvchi dastur tuzing. Dastur bu raqamlar yig'indisi juft yoki toq bo'ladimi, javobni chop etishi kerak.

# a=int(input('1-sonni kiriting:'))
# b=int(input("2-sonni kiriting: "))
# c=int(input("3-sonni kiriting: "))
#
# natija = a+b+c
# if natija % 2 ==0: print(f"{natija} juft")
# else: print(f"{natija} toq")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.Agar foydalanuvchi kiritgan raqam beshga karrali bo'lsa, "Salom" ni ko'rsatish uchun dastur yozing, aks holda "Xayr" deb chop eting.
#
# num=int(input("Enter a number: "))
# if num % 5 == 0:
#     print("Salom")
# else:
#     print(" Xayr")

#----------------------------------------------------------------------------------------------------------------------------------
# 4.Oy nomini olgan va o‘sha oy tegishli bo‘lgan faslni (qish, bahor, yoz, kuz) qaytaruvchi dastur tuzing.

# oy=input("Oy nomini kiriting:").lower()
# if oy == "dekabr" or oy == "yanvar" or oy == "fevral": print("qish")
# elif oy == "mart" or oy == "aprel" or oy == "may": print("bahor")
# elif oy == "iyun" or oy == "iyul" or oy == "avgust": print("yoz")
# elif oy == "sentyabr" or oy == "oktyabr" or oy == "noyabr": print("kuz")
# else: print("Ma'lumot mavjud emas!")


#---------------------------------------------------------------------------------------------------------------------------------------------------
# 5.Foydalanuvchidan uchta raqamni so'raydigan va mos keladigan raqamlar sonini ko'rsatadigan dastur yozing.

# a=int(input("1-sonni kiriting: "))
# b=int(input("2-sonni kiriting: "))
# c=int(input("3-sonni kiriting: "))
#
# if a == b ==c : print("Hammasi bir biriga mos")
# elif a == b or a==c or b ==c: print(" Faqat 2tasi mos")
# else: print("Hech qaysi mos emas")
#
#---------------------------------------------------------------------------------------------------------------------------------------------
# Daraja: standart
#
# 1.Dastur tuzingki, agar ikkita tamsayı berilgan bo'lsa, ular ko'paytma 1000 dan katta bo'lmagan taqdirdagina mahsulotini, aks holda yig'indisini qaytaradi.

# a= int(input("1-son kiriting: "))
# b= int(input("2-son kiriting: "))
#
# if a * b <= 1000:
#     print(a * b)
# else:
#     print(a + b)

#-----------------------------------------------------------------------------------------------------------
# 2.Yilni foydalanuvchidan soʻraydigan va yil kabisa yili ekanligini aniqlaydigan dastur yozing, agar Grigoriy kalendariga koʻra, uning soni 4 ga karrali boʻlsa, lekin 100 ga yoki koʻpaytmali boʻlmasa, yil kabisa yil hisoblanadi. 400 dan.
#
# yil = int(input("Istalgan yilni kiriting:"))
#
# if yil % 400 == 0: print( "kabisa yili")
# elif yil % 100 == 0: print ("Oddiy yil")
# elif yil % 4 == 0: print ("Kabisa yili")
# else: print("oddiy yil")

#---------------------------------------------------------------------------------------------------------
# 3.Savollar bilan viktorina:
# 10 ta savoldan iborat qisqa viktorina yarating, unda har bir savolda bir nechta javob variantlari mavjud.
# Foydalanuvchidan har bir savol uchun javob kiritishini so'rang va javoblarning to'g'riligini tekshirish uchun shartli bayonotlardan foydalaning.
# Viktorina oxirida to'g'ri javoblar sonini chop eting.
#
#
# Misol:
#
# Dastur so'raydi: Birinchi jahon urushi qachon boshlandi?
# a - 1914 yil 28 iyul
# b - 1914 yil 29 iyul
# c - 1915 yil 28 iyul
#
# Javbni yozing:
#
# Agar foydalanuvchi to'g'ri javobni (a) kiritsa, dastur "To'g'ri" deb javob beradi.
# va ballar soni 1 ga oshadi
# va 10 ta savoldan keyin dastur to'plangan ballar sonini ko'rsatadi.
#
# Turli mamlakatlarda universitetlarda talabalarning ko'rsatkichlari turlicha amalga oshiriladi: ba'zi joylarda harflar baho sifatida ishlatiladi, boshqalarida esa ular orasidagi yozishmalar quyida keltirilgan:
#
# Samaradorlikni baholash
#
#
# A+ =  5,0
# A = 4,5
# A- = 4,0
# B+ = 3,7
# B = 3,3
# B- = 3,0
# C+ = 2,7
# C = 2,3
# C- = 2
# D+ = 1,7
# D = 1,3
# D- = 1,0
# F = 0
#
# Harf bahosini kiritish sifatida qabul qiladigan va tegishli bahoni sonli ko‘rinishda ko‘rsatadigan dastur tuzing. Noto'g'ri kiritganingizda dastur aniq xato xabari yaratganiga ishonch hosil qiling.
#
#
savollar = [
    {
        "savol": "Birinchi jahon urushi qachon boshlandi?",
        "variantlar": "A)  1914 yil 28 iyul\nB)  1914 yil 29 iyul\nC) 1915 yil 28 iyul\nD) 1918 yil 28 iyul",
        "togri": "A"
    },
    {
        "savol": "Quyosh tizimidagi eng katta sayyora qaysi?",
        "variantlar": "A) Yer\nB) Mars\nC) Yupiter\nD) Venera",
        "togri": "C"
    },
    {
        "savol": "Dunyoning eng katta okeani qaysi?",
        "variantlar": "A) Atlantika\nB) Hind\nC) Tinch\nD) Arktika",
        "togri": "C"
    },
    {
        "savol": "Suvning kimyoviy formulasi qanday?",
        "variantlar": "A) NaCl\nB) H2O \nC) Mg\nD) H",
        "togri": "B"
    },
    {
        "savol": "Dunyodagi eng baland cho'qqi qaysi?",
        "variantlar": "A) Annapurna\nB)Monblan (Fransiya & Italiya) \nC) Kanchenjanga (Nepal Hindiston) \nD) Everest (Jomolungma) ",
        "togri": "D"
    },
    {
        "savol": "Futbol bo'yicha 2022-yilgi jahon chempioni qaysi davlat bo'ldi?",
        "variantlar": "A) Germaniya\nB)Argentina \nC)Hindiston \nD) Italiya",
        "togri": "B"
    },
    {
        "savol": "Kompyuterda ma'lumotlarni saqlash uchun ishlatiladigan qurilma nima?",
        "variantlar": "A) Qattiq disk (HDD) yoki SSD\nB)CD-ROM \nC)USB disk\nD)DVD ",
        "togri": "A"
    },
    {
        "savol": "Suv necha gradusda qaynaydi?",
        "variantlar": "A)100 \nB)1000 \nC)1500 \nD)0 ",
        "togri": "A"
    },
    {
        "savol": "Qaysi dasturiy ta'minot kompaniyasi shtab-kvartirasi Vashington shtatining Redmond shahrida joylashgan?",
        "variantlar": "A)Walmart\nB)Apple \nC)Microsoft \nD)Google",
        "togri": "c"
    },
    {
        "savol": "Amerika qo'shma shtatlari poytaxti qayer?",
        "variantlar": "A)Nyu-York\nB)Vashington \nC)Los-Andjeles\nD)Chikago",
        "togri": "B"
    },

]


samaradorlik = {
    10: "A+",
    9: "A",
    8: "A-",
    7: "B+",
    6: "B",
    5: "B-",
    4: "C+",
    3: "C",
    2: "C-",
    1: "D",
    0: "F"
}

ball = 0


for item in savollar:
    javob = input(f"{item['savol']}\n{item['variantlar']}\nJavobingizni kiriting (A/B/C/D): ").upper()
    if javob == item['togri']:
        print("To'g'ri!\n")
        ball += 1
    else:
        print(f"Noto'g'ri! To'g'ri javob: {item['togri']}\n")

print(f"Siz {ball}/10 ta savolga to'g'ri javob berdingiz.")
print(f"Samaradorlik bahosi: {samaradorlik.get(ball, 'F')}")




#-----------------------------------------------------------------------------------------------------------------------------------
# Daraja: ilg'or
#
# Kvadrat funksiyaning haqiqiy ildizlarini hisoblaydigan dastur tuzing. Avval foydalanuvchidan a, b va c qiymatlarini so'rashingiz kerak. Shundan so'ng, funktsiyaning haqiqiy ildizlari soni va ularning qiymatlari ko'rsatilishi kerak.
# -b   b2-4ac2a
#
# Shokolad to'rtburchaklar shaklida bo'lib, kengligi × uzunlikdagi bo'laklarga bo'lingan. Shokoladni bir marta tekis chiziqda ikki qismga bo'lish mumkin. Aynan x bo'lakdan iborat shokolad bo'lagini shu tarzda sindirish mumkinligini aniqlang. Dastur kirish sifatida uchta raqamni oladi: kenglik, uzunlik, qismlar va YES yoki NO ni chiqarishi kerak.
#
# Itning bir yil umri insonning etti yiliga teng, deb ishoniladi. Ko'pincha itlar ikki yoshga to'lganida to'liq o'sib borishi hisobga olinmaydi. Shunday qilib, ko'pchilik itning hayotining dastlabki ikki yilining har birini inson hayotining 10,5 yiliga tenglashtirishni afzal ko'radi va keyingi barcha yillarni yuqoridagi mantiqni hisobga olgan holda, inson yoshini it yoshiga aylantiradigan dastur yozing.Ikki yoshdan kichik va undan katta itning yoshini qayta hisoblashda dasturning to'g'ri ishlashiga ishonch hosil qiling. Agar foydalanuvchi salbiy raqamni kiritsa, dastur xato xabarini ham ko'rsatishi kerak.
#
