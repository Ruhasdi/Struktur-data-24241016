# memasukkan jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

for _ in range(jumlah_mahasiswa):
    # Input NIM
    nim = input("Masukkan NIM: ")
    
    # Input Nama
    nama = input("Masukkan Nama: ")
    
    # Input mata kuliah dan nilai
    mata_kuliah_nilai = []
    while True:
        mata_kuliah = input("Masukkan nama mata kuliah (atau ketik 'selesai' untuk selesai): ")
        if mata_kuliah.lower() == 'selesai':
            break
        nilai = float(input(f"Masukkan nilai untuk {mata_kuliah}: "))
        mata_kuliah_nilai.append((mata_kuliah, nilai))
    
    # Menyimpan data mahasiswa dalam dictionary
    data_mahasiswa[nim] = {
        'nama': nama,
        'mata_kuliah_nilai': mata_kuliah_nilai
    }

# Menampilkan nilai rata-rata untuk setiap mahasiswa
print("\nRata-rata nilai untuk setiap mahasiswa:")
for nim, info in data_mahasiswa.items():
    total_nilai = sum(nilai for _, nilai in info['mata_kuliah_nilai'])
    jumlah_nilai = len(info['mata_kuliah_nilai'])
    rata_rata = total_nilai / jumlah_nilai if jumlah_nilai > 0 else 0
    print(f"NIM: {nim}, Nama: {info['nama']}, Rata-rata: {rata_rata:.2f}")

# Menampilkan daftar seluruh data mahasiswa
print("\nDaftar seluruh data mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim}, Nama: {info['nama']}, Mata Kuliah dan Nilai: {info['mata_kuliah_nilai']}")