# 1. List Comprehensions
def List_Comprehensions():
    kotak = [x for x in range(5)]
    print(kotak)


# 2. Array 2 Dimensi
def array_2dimensi():
    matrix = [[0 for kolom in range(3)] for baris in range(3)]
    matrix[2][1] = "wawan"
    print(matrix[2][1])


# 3. List Multidimensi
def List_Multidimensi():
    matrix = [[[0 for j in range(3)] for i in range(3)] for h in range(3)]
    matrix[1][2][2] = "wawan"
    print(matrix[1][2][2])


# 4. Fungsi Berparameter
def fungsi_berparameter():
    List_Multidimensi()
    array_2dimensi()
    List_Comprehensions()


# 5. Kuis 1 - List comprehension bilangan genap dikali 3
def kuis1():
    hasil = [x * 3 for x in range(1, 11) if x % 2 == 0]
    print(hasil)


# 6. Kuis 2 - Array 2 dimensi 3x3 dengan angka 1-9
def kuis2():
    matriks = [[(i * 3 + j + 1) for j in range(3)] for i in range(3)]
    for baris in matriks:
        for kolom in baris:
            print(kolom, end=" ")
        print()


# 7. Kuis 3 - Nested list comprehension (flatten list)
def kuis3():
    data = [[2, 4], [6, 8], [10, 12]]
    flat_list = [item for sublist in data for item in sublist]
    print(flat_list)


# 8. Kuis 4 - Fungsi berparameter hitung luas
def kuis4(panjang, lebar):
    return panjang * lebar

hasil = kuis4(8, 5)
print(f"Luas persegi panjang adalah: {hasil}")


if __name__ == "__main__":
    List_Comprehensions()
    array_2dimensi()
    List_Multidimensi()
    fungsi_berparameter()
    kuis1()
    kuis2()
    kuis3()
    hasil = kuis4(8, 5)
    print(f"Luas persegi panjang adalah: {hasil}")
