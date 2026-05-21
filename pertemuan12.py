# Soal 1 - Variable local
print("\nsoal 1")
def penjumlahan(g):
    bilangan = 24
    return g + bilangan

print(penjumlahan(7))


# Soal 2 - Variable di luar fungsi -1
print("\nsoal 2")
bilangan = 12

def perkalian(x):
    return x * bilangan

print(perkalian(7))


# Soal 3 - Variable di luar fungsi -2
print("\nsoal 3")
def perkalian_bilangan(x):
    bilangan = 10
    return x * bilangan

print(perkalian_bilangan(3))


# Soal 4 - Variable global dengan keyword 'global'
print("\nsoal 4")
bilangan = 7
print(bilangan)

def return_bilangan():
    global bilangan
    bilangan = 7
    return bilangan

print(return_bilangan())
print(bilangan)


# Soal 5 - Kuis IMT
print("\nsoal 5")
def hitung_IMT(berat, tinggi):
    return berat / (tinggi ** 2)

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

index_massa_tubuh = hitung_IMT(berat, tinggi)

kategori = (
    (index_massa_tubuh < 18.5, "Kurus"),
    (index_massa_tubuh < 25.0, "Normal"),
    (index_massa_tubuh < 30.0, "Gemuk"),
)

if index_massa_tubuh < 18.5:
    print(f"IMT: {index_massa_tubuh:.2f} - Kurus")
elif index_massa_tubuh < 25.0:
    print(f"IMT: {index_massa_tubuh:.2f} - Normal")
elif index_massa_tubuh < 30.0:
    print(f"IMT: {index_massa_tubuh:.2f} - Gemuk")
else:
    print(f"IMT: {index_massa_tubuh:.2f} - Obesitas")


# Soal 6 - Fungsi segitiga -1
print("\nsoal 6")
def is_segitiga(a, b, c):
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

print(is_segitiga(3, 4, 5))
print(is_segitiga(1, 2, 10))


# Soal 7 - Fungsi segitiga -2
print("\nsoal 7")
def is_segitiga(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

print(is_segitiga(3, 4, 5))
print(is_segitiga(1, 2, 10))


# Soal 8 - Fungsi segitiga -3
print("\nsoal 8")
def is_segitiga(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(is_segitiga(3, 4, 5))
print(is_segitiga(1, 2, 10))


# Soal 9 - Kuis faktorial
print("\nsoal 9")
def faktorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

print(faktorial(5))
print(faktorial(0))
print(faktorial(-1))


# Soal 10 - Kuis Fibonacci
print("\nsoal 10")
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    elem_1 = elem_2 = 1
    hasil_jumlah = 0
    for i in range(3, n + 1):
        hasil_jumlah = elem_1 + elem_2
        elem_1, elem_2 = elem_2, hasil_jumlah
    return hasil_jumlah

# test
for i in range(1, 10):
    print(i, "->", fibonacci(i))


# Soal 11 - Rekursif faktorial
print("\nsoal 11")
def faktorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * faktorial(n - 1)

print(faktorial(5))
print(faktorial(0))


# Soal 12 - Rekursif fibonacci
print("\nsoal 12")
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(24))
