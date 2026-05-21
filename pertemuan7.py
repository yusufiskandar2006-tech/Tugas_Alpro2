#1. indexing list
angka = [1,2,3,4,5]
print("list awal:",angka)

angka[3] = 67
print("list kedua:", angka)

angka[0] = angka[3]
print("list ketiga:",angka)

#2. mengakses isi list
angka = [1,2,3,4,5]
print("isi list:",angka)

angka = [1,2,3,4,5]
print("list ke-3:", angka[3])

#3. fungsi len
angka = [1,2,3,4,5]
print("banyaknya lis:",len(angka))

#4. menghapus elemen dari list
angka = [1,2,3,4,5]
print("sebelum di dell: ",angka)
del angka[0]
print("sesudah di dell: ",angka)

#5. negative indeks
angka = [1,2,3,4,5]
print("manggil pake indeks positif: ",angka[0])
print("mangil pake indeks negative: ",angka[-1])

#6. kuis 19
topi_list = [1,2,3,4,5]
topi_list[len(topi_list)//2] = int(input('masukan angka: '))
del topi_list[-1]
print("banyak elemen: ",len(topi_list))
print("hasil akhir: ",topi_list)

#7. contoh 1 append() dan insert()
angka = [1,2,3,4,5]
print("banyak anggota pada list pertama: ",angka)
angka.append(67)
print("banyak anggota pada list setelah menggunakan fusngsi append:",angka)
angka.insert(0,76)
print("banyak anggota pada list setelah menggunakan fusngsi insert:",angka)

#8. contoh 2
my_list = []
for i in range(5):
    my_list.append(i-1)
print(my_list)    

#9. contoh 2
my_list = []
for i in range(5):
    my_list.insert(2,i-1)
print(my_list)    

#10. menggunakan list
my_list = [1,2,3,4,5]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)    

#11. menggunakan list
my_list = [1,2,3,4,5]
total = 0
for i in (my_list):
    total += i
print(total)   

#12. List in action 2: cobalah yang ada variable my_list, serta yang menggunakan for
my_list = [3, 5, 7, 9, 11]

# Menukar nilai pada indeks ke-0 dan ke-4
my_list[0], my_list[4] = my_list[4], my_list[0]

# Menukar nilai pada indeks ke-1 dan ke-3
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)  # Output: [11, 9, 7, 5, 3]

my_list = [3, 5, 7, 9, 11]
panjang = len(my_list)   # panjang = 5

for i in range(panjang // 2):   # range(2) → i = 0, 1
    # Tukar elemen ke-i dengan elemen ke-(panjang - i - 1)
    my_list[i], my_list[panjang - i - 1] = my_list[panjang - i - 1], my_list[i]

print(my_list)  # Output: [11, 9, 7, 5, 3]

#13. kuis 20
# Langkah 1: Buat list kosong
exo = []
print("Langkah 1:", exo)

# Langkah 2: Tambah 4 anggota pertama dengan append()
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2:", exo)

# Langkah 3: Tambah 7 anggota lain menggunakan loop for
anggota_tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for nama in anggota_tambahan:
    exo.append(nama)
print("Langkah 3:", exo)

# Langkah 4: Hapus Kris, Luhan, Tao (perhatikan pergeseran indeks)
# Setelah langkah 3, indeks: 0=Suho,1=Kai,2=Chanyeol,3=Sehun,4=DO,5=Baekhyun,6=Kris,7=Lay,8=Luhan,9=Tao,10=Chen
del exo[6]   # hapus Kris -> list sekarang panjang 10, Luhan di indeks 8? Mari cek: [Suho,Kai,Chanyeol,Sehun,DO,Baekhyun,Lay,Luhan,Tao,Chen]
del exo[7]   # hapus Luhan (sekarang di indeks 7) -> hasil: [Suho,Kai,Chanyeol,Sehun,DO,Baekhyun,Lay,Tao,Chen]
del exo[7]   # hapus Tao (sekarang di indeks 7) -> hasil: [Suho,Kai,Chanyeol,Sehun,DO,Baekhyun,Lay,Chen]
print("Langkah 4:", exo)

# Langkah 5: Sisipkan Xiumin pada posisi ke-2 dari akhir (indeks -2)
# insert(-2, ...) artinya sebelum dua elemen terakhir
exo.insert(-2, "Xiumin")
print("Langkah 5:", exo)

# Langkah 6: Tampilkan jumlah anggota
print("Jumlah anggota exo:", len(exo))

