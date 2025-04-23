# Meminta input dari pengguna untuk jumlah deret Fibonacci
jumlah_deret = int(input("Masukkan jumlah deret Fibonacci yang ingin ditampilkan: "))

# Inisialisasi variabel untuk menyimpan deret Fibonacci
fibonacci = []

# Inisialisasi dua bilangan pertama dalam deret Fibonacci
a, b = 0, 1

# Perulangan untuk menghasilkan deret Fibonacci
for i in range(jumlah_deret):
    fibonacci.append(b)  # Menambahkan bilangan Fibonacci ke dalam list
    a, b = b, a + b  # Mengupdate nilai a dan b

# Menampilkan deret Fibonacci
print("Deret Fibonacci:", fibonacci)