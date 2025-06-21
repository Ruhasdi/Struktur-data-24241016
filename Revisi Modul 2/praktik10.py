# membuat array
arr = [12, 16, 20, 40, 50, 70] # - Membuat array arr dengan 6 elemen: 12, 16, 20, 40, 50, dan 70.

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr) # - Mencetak string "Array Sebelum Insertion : " dan nilai array arr sebelum penyisipan.

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr)) # - Mencetak string "Panjang Array : " dan panjang array arr sebelum penyisipan. len(arr) akan mengembalikan nilai 6, karena array arr memiliki 6 elemen.

# menyisipkan array pada tengah elemen menggunakan .insert(pos, x)
arr.insert(4, 5) # - Menyisipkan elemen baru dengan nilai 5 pada posisi ke-4 (index 4) dalam array arr. Elemen yang sebelumnya berada pada posisi ke-4 (index 4) dan seterusnya akan bergeser ke kanan.
# Metode insert() digunakan untuk menyisipkan elemen baru pada posisi tertentu dalam array.

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr) # - Mencetak string "Array Setelah Insertion : " dan nilai array arr setelah penyisipan. Array arr sekarang memiliki 7 elemen, dengan elemen baru 5 disisipkan pada posisi ke-4 (index 4).

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr)) # - Mencetak string "Panjang Array : " dan panjang array arr setelah penyisipan. len(arr) akan mengembalikan nilai 7, karena array arr sekarang memiliki 7 elemen.
