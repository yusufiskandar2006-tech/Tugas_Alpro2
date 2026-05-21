#1 Comparison Operator
x = 0
y = 1
z = 0
print(x==y)
print(x==z)
print(x!=z)
print(x!=y)
print(x<y)
print(x>y)
print(y>z)
print(x<=y)
print(x<=z)
print(y<=z)
print(x>=y)
print(x>=z)
print(y>=z)

#2 Kuis 11
n = int(input("masukan nilai n:"))

if n > 100 :
    print(True)
else:
    print(False)

#3 Conditional statement: if tunggal
x = 30

if x == 30:
    print(" x sama dengan 30")

#4 Conditional statement: Rangkaian if
x = 30

if x > 3:
    print(" x lebih besar dari 3")
if x < 456:
    print(" x kurang dari 456")
if x == 30:
    print (" x adalah 30")

#5 Conditional statement: if-else
nilai = int(input(" nilai uas :"))

if nilai < 80:
    print (" aku ga lulus")
else:
    print(" yeayy aku lulus")

#6 Conditional statement: if-elif-else
nilai = int(input("nialai uas :"))
            
if nilai == 80:
    print (" masih luamayan lah")
elif nilai > 80:
    print ("yeayy aku lulus") 
elif nilai == 60:
    print (" kamu harus remedial") 
elif nilai ==10:
    print ("kamu harus ngulang mk")
else:
    print (" gatau lagi nilaiku hancur")      

#7 Membandingkan 2 angka input
angka1 = int(input("enter first number:"))
angka2 = int(input("enter second number:"))

if angka1>angka2:
    angka_terbesar = angka1
else:
    angka_terbesar = angka2

print("angka terbesar:",angka_terbesar)

#8 kuis 12
angka1 = int(input("enter the first number:"))
angka2 = int(input("enter the second number:"))
angka3 = int(input("enter the trhird number:"))

if angka1 > angka2:
    angka_terbesar = angka1
elif angka2 > angka3:
    angka_terbesar = angka2
elif angka1 < angka3:
    angka_terbesar = angka3
else:
    angka_terbesar = angka3

print("angka terbesar:",angka_terbesar)

#9 Fungsi max( )
angka1 = int(input("enter the first number:"))
angka2 = int(input("enter the second number:"))
angka3 = int(input("enter the trhird number:"))

angka_terbesar = max (angka1,angka2,angka3)
print("angka terbesar:",angka_terbesar)