#1 literal pada python
print("saya adalah string",type("saya adalah string")) 
print(1297,type(1297))

#2 Buatlah fungsi print() yang berisi literal integer sebelas juta seratus sebelas ribu seratus sebelas. Buatlah juga dalam bentuk positif dan negatif.
print(+11_111_111)
print(-11_111_111)

#3 Additional Convention: Buatlah fungsi print() yang berisi literal untuk representasi nilai bilangan octal dan hexadecimal
print(0o12) #octal
print(0xFF) #hexadecimal

#4 Float: Buatlah fungsi print() yang berisi literal float 0.4 dan 4.0; buat juga bentuk lainnya tanpa memasukkan angka 0; Buat juga dengan nilai float menggunakan nilai eksponensial
print(0.4)
print(4.0)
print(.4)
print(4.)
print(4e-1)
print(0.4e1)

#5 String: Buatlah fungsi print() yang berisi literal string dengan petik 2 (“ “) dan petik satu (‘ ‘)
print("saya petik 2",type("saya petik 2"))
print('saya petik 1',type('saya petik 1'))

#6 Boolean Values: Buatlah fungsi print yang berisi literal Bolean 
print(10>5,type(10>5))
print(5>10,type(5>10))

#7 Operator Pangkat: Buatlah 4 print yang berisi operasi pemangkatan 2 buah literal: integer-integer, integer-float, float-integer, float-float
#int ** int
print(2 ** 3,   type(2 **3 ))
#int ** float
print(2 ** 3.0, type(2** 3.0))
#float ** int
print(2.5 ** 2, type(2.5 ** 2))
#float ** float
print(4.0 ** 0.5, type(4.0 ** 0.5))

#8 Operator Perkalian: Buatlah 4 print yang berisi operasi perkalian 2 buah literal: integer-integer, integer-float, float-integer, float-float
#int * int
print(5 * 3, type(5 * 3))
#int * float
print(4 * 2.5, type(4 * 2.5))
#float * int
print(0.5 * 10, type(0.5 * 10))
#float * float
print(1.5 * 2.5, type(1.5 * 2.5))

#9 Operator Pembagian: Buatlah 4 print yang berisi operasi pembagian 2 buah literal: integer-integer, integer-float, float-integer, float-float
#int / int
print(5 / 2, type(5 / 2))
#int / float
print(10 / 4.0, type(10 / 4.0))
#float / int
print(10.5 /2, type(10.5 / 2))
#float / float
print(12.0 / 3.0, type(12.0 / 3.0))

#10 Operator pembagian integer: Buatlah 4 print yang berisi operasi pembagian integer atau floor division 2 buah literal: integer-integer, integer-float, float-integer, float-float
#int // int
print(10 // 3, type(10 // 3))
#int // float
print(10 // 4.0, type(10 // 4.0))
#float // int
print(10.5 // 2, type(10.5 // 2))
#float // float
print(12.0 // 5.0, type(12.0 // 5.0))

#11 Operator Modulo: Buatlah 4 print yang berisi operasi modulo 2 buah literal: integer-integer, integer-float, float-integer, float-float
#int % int
print(10 % 3, type(10 % 3))
#int % float
print(10 % 4.0, type(10 % 4.0))
#float % int
print(12.5 % 5, type(12.5 % 5))
#float % float
print(7.5 % 2.5, type (7.5 % 2.5))

#12 Operator Unary dan Binary: 
print("--- Unary ---")
print(-100)
print(+50)
print(--20)
print(++20)
print("--- Unary ---") 
print(10+5)
print(20-7)
print(4*3)
print(8/2)
print(2 ** 3)
print(8 // 3)
print(10 % 3)

#13 Subekspresi
print (2+3*4)
print ((2+3)*4)
print(10+(5*(10-8)))
print((20//3)+(2**3))

#14 kuis 
print( (2 ** 4 ), (2 * 4.), (2 * 4))
print( (-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print( (2 % -4), (2 % 4), (2 ** 3 ** 2))