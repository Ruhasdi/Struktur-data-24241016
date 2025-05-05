aku = {
    "nama": "Adam Bachtiar Maulachela",
    "url:" "https://www.fsttundikma.id"
}

# contoh jika 1 item
nama_dict = {
    "key": "value"
}

# contoh jika lebih dari 1 item
nama_dict = {
    "key1": "value",
    "key2": "value",
    "key3": "value"
}

# membuat dictionary
dict = {
    "nama"      : "Adam Bachtiar Maulachela",
    "NIDN"      : 62708078505,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : "@adamMaulachela",
        "twiter"    : '_',
        "instagram" : '-'
    }
}

# mengakses dict menggunakan key
print("Nama Saya adalah %s" % dict['nama'])
print("Akun Github saya %s" % dict['sosmed']['Github'])

# cara lainnya dengan menggunakan .get
print("NIDN Saya adalah %s" % dict.get('NIDN'))

nama_dict['kunci'] = 'Nilai_baru'

# Mengubah nilai item dictionary dict dengan key
data['status'] = False

# Cek hasil perubahan
print(data['status'])

# Mengubah nilai item dictionary dengan .update
data.update({"sosmed" : {"twitter" : "@adammaulachaila"}})

# cek hasil perubahan
print(data['sosmed']['twitter'])

# Menghapus menggunakan perintah del
del data['status']

# cek hasil penghapusan data 
print(data)

# Menghapus item menggunkan method pop()
data.pop("sosmed")

# cek hasil penghapusan data 
print(data)

# membuat dictionary
mahasiswa = {
    "name" : "Adam Bachtiar Maulachela"
}

# menambahkan nim
mahasiswa.update({
    "nidn" : "0708078505"
})

# melihat hasilnya
print(mahasiswa)

# mencetak data pada dict secara berulang-ulang setiap key
for key in mahasiswa:
    print(key, mahasiswa[key])

# Atau:
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

data_mahasiswa = {
    "NIM001": {"nama": "Rina", "jurusan": "TI"},
    "NIM002": {"nama": "Budi", "jurusan": "SI"}
}

data_mahasiswa = {}
jumlah = int(input("Jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")
    data_mahasiswa[nim] = {
        "nama": nama,
        "jurusan": jurusan
    }

data_mahasiswa["22001"] = {"nama": "Rina", "jurusan": "TI"}
print("\nCari data mahasiswa")
cari = input("Masukkan NIM: ")
if cari in data_mahasiswa:
    mhs = data_mahasiswa[cari]
    print(f"Nama: {mhs['nama']}, Jurusan: {mhs['jurusan']}")
else:
    print("Mahasiswa tidak ditemukan.")

print("\nDaftar Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} → {info['nama']} ({info['jurusan']})")

NIM: 22001 → Rina (TI)
Jumlah mahasiswa: 2

Mahasiswa ke-1:
NIM: 22001
Nama: Rina
Jurusan: TI

Mahasiswa ke-2:
NIM: 22002
Nama: Budi
Jurusan: SI

Masukkan NIM: 22001

Nama: Rina, Jurusan: TI

Daftar Seluruh Mahasiswa:
NIM: 22001 → Rina (TI)
NIM: 22002 → Budi (SI)

