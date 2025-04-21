# function
def sapa ():
    print("halo, selamat datang!")

# penampilan function 
sapa()
sapa()
sapa()
sapa()

# function dengan argumen atau parameter 
# function dengan 1 parameter
def sapa_nama(nama):
    print(f"Halo, {nama}!")

# Pemanggilan Function
sapa_nama("Adam")

# function dengan lebih dari 1 parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)

# Pemanggilan Function
luas_segitiga(4, 6)

def tambah(a, b):
    return a + b

# pemanggilan fungsi
hasil = tambah(3, 5)
print("Hasil:", hasil)

# contoh lain function dengan return dan parameter
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# pemanggilan fungsi
print(f"Luas Persegi : {luas_persegi(6)}")

# menjadikan fungsi sebagai inputan buat fungsi lainnya 
# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# pemanggilan fungsi
print(f"Volume Persegi = {volume_persegi(6)}")

def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')
    
# pemanggilan function, dengan 1 argumen
student("Wallberg")

# pemanggilan function, dengan 3 argumen
student('John', 'Gates', 'Seventh')  

# pemanggilan function dengan 2 argumen
student('John', 'Gates')                  
student('John', 'Seventh')

def kali(a: int, b: int) -> int:
    return a * b

# Pemanggilan function
print("Hasil = " ,kali(3, 4))
print("Tipe Data : ", type(kali(3,4)))

# *args untuk argumen bervariasi
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Selamat Datang', 'Di', 'PTI UNDIKMA')

# function dengan **kwargs 
def info_mahasiswa(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

# Pemanggilan function
info_mahasiswa(nama="Rina", jurusan="TI", angkatan=2022)

# kombinasi syntax *args dan **kwargs dalam satu function
def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Pemanggilan function
fun(1, 2, 3, a=4, b=5)

nama = "Budi"  # variabel global

def sapa():
    print("Halo,", nama)

# memanggil function
sapa()

nama = "UNDIKMA"
versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.2"
    # mengakses variabel lokal
    print ("Nama: %s" % nama)
    print ("Versi: %s" % versi)


# mengakses variabel global
print ("Nama: %s" % nama)
print ("Versi: %s" % versi)

# memanggil fungsi help()
help()