# Jumlah baris yang diinginkan
n = 5

# Perulangan untuk setiap baris
for i in range(n):
    # Menghitung jumlah bintang yang akan ditampilkan
    # Hanya menampilkan bintang pada baris ganjil
    if i % 2 == 0:  # Baris ganjil dalam indeks (0, 2, 4, ...)
        print('*' * (2 * i + 1))  # Menampilkan bintang sesuai dengan baris