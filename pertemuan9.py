#1.	Bubble sort
my_list = [57, 13, 56, 12, 3]  # list untuk diurutkan
swapped = True              # Inisiasi awal, untuk memasuki loop

while swapped:
    swapped = False         # Untuk mengindikasi bahwa tidak ada proses penukaran elemen
    for i in range(len(my_list) - 1):  # Perulangan sepanjang banyaknya elemen
        if my_list[i] > my_list[i + 1]:  # Membandingkan elemen saat ini dengan elemen berikutnya
            swapped = True               # Akan ada proses penukaran
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Proses penukaran

print(my_list)  # Mencetak isi list

#2.	Interactive Bubble sort
def bubble_sort2():
    my_list = []
    swapped = True
    num = int(input("Masukkan panjang elemen list yang akan diurutkan: "))
    
    for i in range(num):
        val = float(input("Masukkan elemen list: "))
        my_list.append(val)
    
    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                swapped = True
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    
    print("\nSorted:")
    print(my_list)

bubble_sort2()

#3.Method sort
def method_sort():
    my_list = [23,3,4,6,7,]
    my_list.sort(key=lambda x: x)
    print(my_list)

method_sort()

#4.	Method Reverse
def method_reverse():
    my_list = [23,3,4,6,7,]
    my_list.reverse()
    print(my_list)

method_reverse()

#5.	The inner life of list - 1
def The_inner_life_of_list_1():
    list_1 = [1]
    list_2 = list_1
    list_1[0] = 2
    print(list_2)

The_inner_life_of_list_1()

#6.	Slice – 1: [awal:akhir]
def slice_example():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    new_list = my_list[1:4]   # mengambil indeks 1, 2, 3 (indeks 4 tidak termasuk)
    print(new_list)

slice_example()

#7.	Slice – 2: [positif:negative]
def slice2():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    new_list = my_list[1:-1]   # dari indeks 1 hingga sebelum indeks terakhir
    print(new_list)

slice2()

#8.	Slice – 3: [negative:positif]
def slice3():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    new_list = my_list[-2:3]   # dari indeks -2 (nilai 6) hingga indeks 3 (nilai 4), tetapi start > stop
    print(new_list)

slice3()

#9.	Slice – 4: [:akhir]
def slice4():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    new_list = my_list[:3]   # dari awal hingga sebelum indeks 3
    print(new_list)

slice4()

#10. Slice – 5: [awal:]
def slice5():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    new_list = my_list[2:]   # dari indeks 2 hingga akhir list
    print(new_list)

slice5()

#11. Slice – 6: [:]
def slice6():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    new_list = my_list[:]   # mengambil seluruh elemen dari awal hingga akhir
    print(new_list)

slice6()

#12. Menghapus slice
def del_slice():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    del my_list[0:2]   # menghapus elemen indeks 0 dan 1
    print(my_list)

del_slice()

#13. Menghapus semua elemen list
def del_slice2():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    del my_list[:]   # menghapus semua elemen list
    print(my_list)

del_slice2()

#14. Menghapus list
def del_list():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    del my_list      # menghapus objek list itu sendiri
    print(my_list)   # akan error karena my_list sudah tidak terdefinisi

del_list()

#15. Penggunaan operator in
def operator_in():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print(5 in my_list)      # True karena 5 ada dalam list
    print(5 not in my_list)  # False karena 5 ada, jadi "tidak ada" salah
    print(22 in my_list)     # False karena 22 tidak ada

operator_in()

#16. Penggunaan oprator not in
def operator_in():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print(5 in my_list)
    print(5 not in my_list)
    print(22 in my_list)

operator_in()

#17. Simple program dari list – 1
def simple_program_dari_list_1():
    my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
    largest = my_list[0]  # mulai dari elemen pertama

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    print(largest)

simple_program_dari_list_1()

#18. Simple program dari list – 2
def simple_program_dari_list_2():
    my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
    largest = my_list[0]  # perbaiki: tanpa kutip

    for i in my_list: #tanpa len
        if i > largest:
            largest = i

    print(largest)

simple_program_dari_list_2()

#19. Simple program dari list – 3
def Simple_program_dari_list_3():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    to_find = 5
    found = False

    for i in range(len(my_list)):
        found = my_list[i] == to_find
        if found:
            break

    if found:
        print("Elemen ditemukan pada index ke-", i)
    else:
        print("Tidak ada di dalam list")

Simple_program_dari_list_3()

#20 kuis 21
def kuis_21():
    tebakan = [3, 7, 11, 42, 34, 49]
    hasil_undian = [5, 9, 11, 42, 3, 49]

    # Mencari angka yang ada di kedua list
    cocok = 0
    for angka in tebakan:
        if angka in hasil_undian:
            cocok += 1

    print(f"Anda menebak benar sebanyak: {cocok} kali")

kuis_21()

#21 kuis 22
def kuis_22():
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    temp_list = []

    for angka in my_list:
        if angka not in temp_list:
            temp_list.append(angka)

    print("List unik:", temp_list)

kuis_22()