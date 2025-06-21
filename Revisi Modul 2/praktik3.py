# impor library numpy
import numpy as np

# membuat array
a = np.array([1, 2, 3]) # Membuat array a dengan 3 elemen: 1, 2, dan 3.
b = np.array([4, 5, 6]) # Membuat array b dengan 3 elemen: 4, 5, dan 6.

# menggunakan operasi penjumlahan pada 2 array
print(a + b)       # array([5, 7, 9]) # Melakukan operasi penjumlahan elemen-wise antara array a dan b.
# Hasilnya adalah array baru dengan elemen-elemen yang merupakan hasil penjumlahan elemen-elemen yang sesuai dari array a dan b.
# Output: [5 7 9]

# Indexing dan Slicing pada Array
arr = np.array([10, 20, 30, 40]) # Membuat array arr dengan 4 elemen: 10, 20, 30, dan 40.
print(arr[1:3])    # array([20, 30]) # Melakukan slicing pada array arr untuk mendapatkan elemen-elemen dari indeks 1 hingga 3 (tidak termasuk indeks 3).
# Hasilnya adalah array baru dengan elemen-elemen yang sesuai dari array arr.
# Output: [20 30]

# iterasi pada array 
for x in arr: # Melakukan iterasi pada array arr untuk mengakses setiap elemen secara berurutan.
    print(x) # Mencetak nilai elemen yang sedang diakses dalam iterasi.
#Output:10,20,30,40