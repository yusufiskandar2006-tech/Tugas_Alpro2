# 1.Perulangan dengan while, contoh 1
while True:
    print("infinity looping")

# 2.Perulangan dengan while, contoh 2
i = 1
while i <= 5:
    print(i)
    i += 1

# 3.Contoh kasus menghitung angka ganjil dan genap dengan perulangan while    
ganjil = 0
genap = 0

print("Masukkan angka (0 untuk berhenti):")
while True:
    angka = int(input("Angka: "))
    if angka == 0:
        break           # keluar dari perulangan jika input 0
    if angka % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print("\nHasil perhitungan:")
print(f"Angka genap : {genap}")
print(f"Angka ganjil: {ganjil}")

# 4.Kuis 15: Implementasi while
secret_number = 777

print(
    """
+===============================================+
| Selamat datang di game saya, muggle!          | 
| masukkan suatu angka dan tebak                |
| angka berapa yang saya pilih                  |
| untuk kamu.                                   |
| Jadi, berapa angka rahasianya?                | 
+===============================================+
"""
)

# Lanjutkan kode disini
while True:
    try:
        tebakan = int(input("Masukkan angka: "))
    except ValueError:
        print("Input harus berupa angka bulat!")
        continue

    if tebakan == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break
    else:
        print("hahaha ! kamu nyangkut deh di Loop saya")


# 5.Perulangan dengan for, contoh 1: bandingkan nilai a,b,c,d,e
# CONTOH 1

# range(10) menghasilkan angka 0 sampai 9 (stop=10, start default 0)
for a in range(10):
    print("nilai a saat ini adalah", a)

# range(2,8) menghasilkan angka 2 sampai 7 (start=2, stop=8)
for b in range(2, 8):
    print("nilai b saat ini adalah", b)

# range(2,8,3) menghasilkan angka 2, 5 (start=2, stop=8, step=3)
for c in range(2, 8, 3):
    print("nilai c saat ini adalah", c)

# range(1,1) start=1, stop=1, tidak ada angka karena start >= stop
for d in range(1, 1):
    print("nilai d saat ini adalah", d)  # tidak akan pernah dicetak

# range(2,1) start=2, stop=1, juga tidak menghasilkan angka
for e in range(2, 1):
    print("nilai e saat ini adalah", e)  # tidak akan pernah dicetak

# 6.Perulangan dengan for, contoh 2: menghitung eksponensial 2    
kuadrat = 1
for angka in range (11):
    print("2 pangkat",angka,"adalah",kuadrat)
    kuadrat *= 2

# 7.Contoh break dan continue.    
# CONTOH BREAK DAN CONTINUE

print("Instruksi break:")
for i in range(1, 6):
    if i == 3:
        break          # hentikan loop sepenuhnya saat i = 3
    print("Bagian ini ada di dalam loop.", i)
print("Bagian ini ada di luar loop.")

print("\nInstruksi continue:")
for i in range(1, 6):
    if i == 3:
        continue       # lewati sisa kode untuk i = 3, lanjut ke i berikutnya
    print("Bagian ini ada di dalam loop.", i)
print("Bagian ini ada di luar loop.")

# 8.Kuis 16: implementasi break
secret_number = 999

print(
    """
+===============================================+
| Selamat datang di game saya, muggle!          | 
| masukkan suatu angka dan tebak                |
| angka berapa yang saya pilih                  |
| untuk kamu.                                   |
| Jadi, berapa angka rahasianya?                | 
+===============================================+
"""
)

# Lanjutkan kode disini
while True:
    try:
        tebakan = int(input("Masukkan angka: "))
    except ValueError:
        print("Input harus berupa angka bulat!")
        continue

    if tebakan == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break
    else:
        print("hahaha ! kamu nyangkut deh di Loop saya")

# 9.Kuis 17: Implementasi continue.   
     # Meminta user memasukkan sebuah kata
kata = input("Masukkan sebuah kata: ")

# Mengubah kata menjadi huruf kapital
kata = kata.upper()

print("Huruf konsonan dari kata tersebut:")

# Loop for untuk setiap karakter dalam kata
for huruf in kata:
    # Percabangan if-elif-else untuk memeriksa vokal
    if huruf == 'A':
        continue  # "memakan" huruf vokal A
    elif huruf == 'I':
        continue  # "memakan" huruf vokal I
    elif huruf == 'U':
        continue  # "memakan" huruf vokal U
    elif huruf == 'E':
        continue  # "memakan" huruf vokal E
    elif huruf == 'O':
        continue  # "memakan" huruf vokal O
    else:
        # Jika bukan vokal (konsonan atau karakter lain), cetak huruf tersebut
        print(huruf, end=" ")
print() 

# 10.Perulangan while dengan else
#contoh 1
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:",i)    

#contoh 2 
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:",i) 

# 11.Perulangan for dengan else    
#contoh 1
i  = 333
for i in range (5):
    print(i)
else:
   print("else:",i)
#contoh 2
i  = 333
for i in range (3,1):
    print(i)
else:
   print("else:",i)

# 12.Contoh ekspresi logika pada python
a = 10
b = 30
print(a is not b,type(a is not b))

# 13.Operasi logical vs. Bit pada python
# Nilai awal
i = 15
j = 22

# Operator logika AND
# Python: and mengembalikan operand kedua jika yang pertama truthy, 
# karena i = 15 (truthy) maka hasilnya adalah j = 22
log = i and j
print("log =", log)  # Output: 22

# Operator bitwise AND
# Melakukan operasi AND pada level bit
# i = 15 (biner: 00001111), j = 22 (biner: 00010110)
# Hasil AND: 00000110 = 6
bit = i & j
print("bit =", bit)  # Output: 6

# Operator logika NOT
# Mengembalikan kebalikan boolean dari nilai i
# i = 15 (truthy) -> not i = False
logneg = not i
print("logneg =", logneg)  # Output: False

# Operator bitwise NOT (komplemen)
# Dalam Python, ~i = -(i+1) karena representasi komplemen dua
# ~15 = -16
bitneg = ~i
print("bitneg =", bitneg)  # Output: -16

# 14.Binary Shifting
a = 100
a_right = a >> 1
a_left = a << 2
print(a,a_right,a_left)

# 15.Kuis 18: Latihan Bitwise operator dan Binary Shifting 
x = 4
y = 1

a = x & y   # Operasi bitwise AND
b = x | y   # Operasi bitwise OR
c = ~x      # Operasi bitwise NOT (komplemen)
d = x ^ 5   # Operasi bitwise XOR
e = x >> 2  # Operasi shift kanan (right shift)
f = x << 2  # Operasi shift kiri (left shift)

print(a, b, c, d, e, f)

