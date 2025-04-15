# Meminta input dari pengguna untuk jumlah deret
jumlah_deret = int(input("Masukkan jumlah deret bilangan genap yang ingin ditampilkan: "))

# Inisialisasi variabel untuk menyimpan bilangan genap
bilangan_genap = []

# Perulangan untuk menghasilkan bilangan genap
for i in range(1, jumlah_deret + 1):
    bilangan_genap.append(i * 2)  # Menghitung bilangan genap

# Menampilkan deret bilangan genap
print("Deret bilangan genap:", bilangan_genap)