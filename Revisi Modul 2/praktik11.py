# membuat array
a = [10, 20, 30, 40, 50] # Membuat array a dengan 5 elemen: 10, 20, 30, 40, dan 50.
print("Array Sebelum Deletion : ", a) # Baris ini dikomentari, sehingga tidak akan dieksekusi. Jika tidak dikomentari, maka akan mencetak string "Array Sebelum Deletion : " dan nilai array a sebelum penghapusan.

# menghapus elemen array pertama yang nilainya 30
a.remove(30) # Menghapus elemen pertama yang nilainya 30 dari array a. Metode remove() digunakan untuk menghapus elemen pertama yang memiliki nilai tertentu.
print("Setelah remove(30):", a) # Mencetak string "Setelah remove(30):" dan nilai array a setelah penghapusan elemen 30. Array a sekarang memiliki 4 elemen: 10, 20, 40, dan 50.

# menghapus elemen array pada index 1 (20)
popped_val = a.pop(1) # Menghapus elemen pada index 1 (20) dari array a dan mengembalikan nilai elemen yang dihapus. Metode pop() digunakan untuk menghapus elemen pada index tertentu dan mengembalikan nilai elemen yang dihapus.
# Nilai elemen yang dihapus (20) disimpan dalam variabel popped_val.
print("Popped element:", popped_val) # Mencetak string "Popped element:" dan nilai elemen yang dihapus (20).
print("Setelah pop(1):", a) # Mencetak string "Setelah pop(1):" dan nilai array a setelah penghapusan elemen pada index 1. Array a sekarang memiliki 3 elemen: 10, 40, dan 50.

# Menghapus elemen pertama (10)
del a[0] # Menghapus elemen pertama (10) dari array a. Perintah del digunakan untuk menghapus elemen pada index tertentu.
print("Setelah del a[0]:", a) # Mencetak string "Setelah del a[0]:" dan nilai array a setelah penghapusan elemen pertama. Array a sekarang memiliki 2 elemen: 40 dan 50.
