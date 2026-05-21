#1 Membuat fungsi input kemudian tampilkan ke konsol
print("masukan nama")
anything = input()
print ("selamat datang",anything)

#2 Membuat fungsi input dengan argumen
anything = input()
print ("welcome to school",anything)

#3 Memahami hasil dari fungsi input
anything = input("enter a number:")
something = anything ** 3
print (anything,"to the power of 2 is",something)

#4 Mengkonversi tipe data 1: Membuat konversi tipe data float pada fungsi input
anything =float(input("enter a number : "))
something = anything ** 2.0
print (anything,"to the power of 2 is",something)

#5 Mengkonversi tipe data 2: Membuat program untuk menghitung sisi miring segitiga dengan variable hypo untuk menampung hasil rumus pitagoras
leg_a = float(input("input first leg length:"))
leg_b = float(input("input second leg length: "))
hypo = (leg_a ** 2 + leg_b ** 2) **.5
print("hyputenuse length is",hypo)

#6 Mengkonversi tipe data 2: Membuat program untuk menghitung sisi miring segitiga tanpa membuat variable untuk menampung hasil operasi
leg_a = float(input("input first leg length:"))
leg_b = float(input("input second leg length: "))
print("hyputenuse length is",(leg_a ** 2 + leg_b ** 2) **.5)

#7 Operator Konkatenasi
nama_depan = "budi"
nama_belakang = "santoso"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

#8 Operator Replikasi
print("=" * 30)
print("laporan keungan bulanan")
print("=" * 30)

#9 Mengkonversi Tipe data 3: konversi ke string 
leg_a = float(input("input first leg length:"))
leg_b = float(input("input second leg length: "))
print("hyputenuse length is"+str((leg_a ** 4 + leg_b ** 3) **.8))

#10 Melihat tipe data dari suatu variable
x = 2.674
print(type(x))

#11  kuis 7
a = float(input("masukan nialai variabel a:"))
b = float(input("masukan nialai variabel b:"))

penjumlahan = a+b
pengurangan =a-b
perkalian  =a*b
print(f"\n hasil penjumlahan ({a} + {b}) = {penjumlahan}")
print(f" hasil pengurangan ({a} - {b}) = {pengurangan}")
print(f" hasil perkalian ({a} * {b}) = {perkalian}")

if b != 0 :
    pembagian = a /b
    print(f" hasil pembagian ({a} / {b} = {pembagian}")
else:
    print(f" hasil pembagian ({a} / {b} =tidak bisa membagi")  
print("\n SELAMAT KAMU SUDAH PINTAR MTK")

#12 kuis 8
x = float(input("Masukan nilai x:"))
y = 1.0 /(x+1.0/(x+1.0(x+1.0)))
print("nilai y adalah",y)

#13 kuis 9
jam =int(input("waktu mulai (jam):"))
menit =int(input("waktu mulai (menit):"))
durasi =int(input("durasi acara (menit):"))

total_menit = menit + durasi
jam_selesai =jam + total_menit // 60
menit_selesai = total_menit % 60

print("waktu selesai acara:",jam_selesai,":",menit_selesai)

