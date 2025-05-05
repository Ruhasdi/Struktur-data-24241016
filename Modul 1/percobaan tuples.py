# cara membuat tuple singleton
satu = ('Isi',)
dua = "ini adalah tuple?",

# cek tipe datanya
print(type(satu))
print(type(dua))

# jika tidak pakai koma
satu = ('Isi')
dua = "ini adalah tuple?"

# cek tipe datanya
print(type(satu))
print(type(dua))

# membuat tuple
nama = ('Adam', 'Bachtiar', 'Maulachela')

# mengakses indeks ke 1 dari tuple
print(nama[1])

# Membuat Tuple
t = (1, 5, 10, 15)

# mengubah isi elemen tuple
t[0] = 0

# membuat tuple
angka = (10, 20, 30, 40)

# Memotong tuple
print(angka[1:3]) 
print(angka[:2])
print(angka[2:])

# Operasi pada tuple
# penggabungan tuple
print((1, 2) + (3, 4))

# pengulangan tuple
print(('A',) * 3)

# cek panjang tuple
data = (1, 2, 4, 5)
print(len(data))

# cek keanggotaan tuple
print(3 in data)

# Nested Tuple atau Tuple Bersarang
t = (1, 2, (3, 4))
print(t[2][0])  # Output: 3

tuple1 = "aku", "mahasiswa", "PTI UNDIKMA"
tuple2 = "selama", 3, "tahun"
tuple3 = (tuple1, tuple2) # <- nested tuple

print(tuple3)

# tuple berisi list
t = ([1,2,3,4], True)

print (t)

# Sequence Unpacking
# pertama buat tuple seperti ini
web = 123, "PTI UNDIKMA", "https://fsttundikma.id"

# lalu di-unpacking
id_web, nama, url = web

# maka sekarang tiga variabel tersebut akan bernilai
# sesuai yang ada di dalam tuple
#
# mari kita cetak
print(id_web)
print(nama)
print(url)

# Latihan tuple 
matkul_list = []
jumlah = int(input("Input jumlah mata kuliah: "))

for i in range(jumlah):
    print(f"\nMata kuliah ke-{i+1}:")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks = int(input("SKS: "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)

# Tampilkan data
print("\nDaftar Mata Kuliah:")
for m in matkul_list:
    print(m)

total_sks = sum(m[2] for m in matkul_list)
print(f"\nTotal SKS: {total_sks}")