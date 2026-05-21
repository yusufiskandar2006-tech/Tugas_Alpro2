#1 Membuat dan menggunakan variable: Buat variable var, nilai dan nama_mahasiswa seperti contoh
var = 2530801064
nilai = 4.0
nama_mahasiswa = 'yusuf iskandar'
print(var,type(var))
print(nilai,type(nilai))
print(nama_mahasiswa,type(nama_mahasiswa))
print(var,nilai,nama_mahasiswa)

#2 Membuat dan menggunakan variable: buat variable Nama dengan nilai “Budi”, tampilkan veriabel nama
Nama = "budi"
print(Nama) #ouputnya "budi"
print(nama) #outputnya error

#3 Memasukkan nilai baru ke variable yang sudah ada: Buat variable umur, kemudian beri nilai baru ke variable umur, seperti contoh
umur = 19
umur +=2
print("unur:",umur)

#4 Memasukkan nilai baru ke variable yang sudah ada: Buat variable umur, kemudian beri nilai baru ke variable umur, seperti contoh
tabungan = 1_000_000
tabungan += 2_000_000
print(tabungan)

#5 Shortcut Operators
rupiahtodolar = 6000
rupiahtodolar += 11_000
print(rupiahtodolar)

tabungan = 1_000_000
tabungan -= 500000
print(tabungan)

cookies = 90
cookies /= 2
print(cookies)

bayarmakan = 50000
bayarmakan *= 2
print(bayarmakan)

#6 Solving Simple Mathematical Problem
#skor awal
skor = 100
#user dapet bonus 20
skor += 20
#user kena pinalti 10
skor -= 10
#skor user dikali 2
skor *= 2
print("skor akhir pemain adalah :", skor)

#7 kuis 3
Ayu = 50000
Bagus = 75000
Citra = 100000
print(Ayu,Bagus,Citra=",")
jumlah_tabungan = Ayu + Bagus + Citra
print("Jumlah tabungan adalah:",jumlah_tabungan)

#8 kuis 4
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#9 kuis 5
x = float(input("masukan nilai x:"))
y = 3*(x**3) - 2*(x**2) + 3*x -1 
print("Y = ", y)