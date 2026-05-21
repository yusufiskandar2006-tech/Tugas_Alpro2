# SOAL 1 - Membuat tuple dan tampilkan

tuple_1 = (1, 2, 3)
tuple_2 =  4, 5, 6
tuple_kosong = ()
print(tuple_1)
print(tuple_2)
print(tuple_kosong)


# SOAL 2 - Menggunakan tuple

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[:1])
print(my_tuple[:-2])

for element in my_tuple:
    print(element)


# SOAL 3 - Memodifikasi tuple

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

my_tuple.append(6)
print(my_tuple)

del my_tuple
print(my_tuple)

my_tuple [1] = -10
print(my_tuple)


# SOAL 4 - Menggunakan tuple dengan len(), +, *, in dan not in

my_tuple = (1, 2, 3, 4, 5)

t1 = my_tuple + (6, 5)
t2 = my_tuple * 2

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


# SOAL 5 - Penugasan simultan pada tuple

pribumi = [("ucup", 123), ("robi", 456), ("kalin", 789), ("abil", 999)]
for nama, nomer in pribumi:
    print(f"Nama: {nama}, Nomer: {nomer}")


# SOAL 6 - Membuat dictionary dan tampilkan
# SOAL 7 - Mengakses isi dictionary
# SOAL 8 - Method keys()

class Nomer:
    def __init__(self):
        self.lis = {}

class Child(Nomer):
    def __init__(self):
        super().__init__()

    def tambah(self, nama, nomer):
        self.lis[nama] = nomer

    def akses(self, nama):
        if nama in self.lis:
            print(f"Ketemu! Nomer {nama} adalah: {self.lis[nama]}")
            return True
        return False

    def metod(self):
        for nama in self.lis.keys():
            return nama

    def cetak(self):
        print(f"Hasilnya: {self.lis}")

pribumi = [("ucup", 123), ("robi", 456), ("kalin", 789), ("abil", 999)]
objek = []

for nama, nomer in pribumi:
    obj = Child()
    obj.tambah(nama, nomer)
    objek.append(obj)

for orang in objek:
    orang.cetak()

tayo = input("Masukkan nama kontak: ")
ketemu = False

for orang in objek:
    if orang.akses(tayo):
        ketemu = True
        break

if not ketemu:
    print(f"Yah, '{tayo}' nggak ada di kontak wirl")

kontak = []
for orang in objek:
    haha = orang.metod()
    kontak.append(haha)
print(f"Kontak versi keys: {kontak}")


# SOAL 9 - Method values()

nilai = {"Kalin": 85, "Yusuf": 90, "Abil": 95, "Hamdi": 80}

for angka in nilai.values():
    print(angka)


# SOAL 10 - Method items()

idol = {"cortis": "martin", "txt": "soobin", "nct dream": "mark lee"}
for grup, leader in idol.items():
    print(grup, "leadernya adalah", leader)


# SOAL 11 - Method update()

idol = {"cortis": "martin", "txt": "soobin", "nct dream": "mark lee"}

idol.update({"exo": "suho"})

for grup, leader in idol.items():
    print(grup, "leadernya adalah", leader)


# SOAL 12 - Method popitem()

x = {"1": "saya", "2": "kamu", "3": "dia"}
print(x.popitem())


# SOAL 13 - Modifikasi dictionary

x = {"1": ["saya"], "2": ["bareng"], "3": ["temen"]}

x["1"].append("lagi")
x["4"] = ["kelas"]
print(x)
del x["4"]
print(x)


# SOAL 14 - Menangani exception

menu = {1: "Tambah data", 2: "Lihat data", 3: "Keluar"}

try:
    pilihan = int(input("Pilih menu (1-3): "))
    if pilihan not in menu:
        raise ValueError("Menu tidak tersedia")
    print(f"Kamu memilih: {menu[pilihan]}")

except ValueError as e:
    print(f"Error: {e}")


# SOAL 15 - Menangani multiple exception

data = {"nama": "Brata", "umur": "20"}

try:
    pilihan = int(input("Pilih (1=nama, 2=umur, 3=nilai): "))
    kunci = ["nama", "umur", "nilai"][pilihan - 1]
    hasil = int(data[kunci]) + 5
    print(f"Hasil: {hasil}")

except ValueError:
    print("Input bukan angka!")
except KeyError:
    print("Data tidak ditemukan!")
except IndexError:
    print("Pilihan di luar menu!")
