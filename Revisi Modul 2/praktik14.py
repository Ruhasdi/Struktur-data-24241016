# impor library numpy
import numpy as np # Mengimpor library NumPy dan memberikan alias np untuk memudahkan penggunaan. NumPy adalah library Python yang digunakan untuk operasi numerik dan matriks.

# Membuat matriks dengan numpy
X = np.array([
    [12,7,3],
    [4,5,6],
    [7,8,9]])
# Membuat matriks X dengan ukuran 3x3 dan elemen-elemen yang ditentukan menggunakan fungsi np.array().
Y = np.array(
    [[5,8,1],
    [6,7,3],
    [4,5,9]])
# Membuat matriks Y dengan ukuran 3x3 dan elemen-elemen yang ditentukan menggunakan fungsi np.array().

# Operasi penjumlahan dua matrik numpy
result = X + Y # Melakukan operasi penjumlahan matriks X dan Y menggunakan operator +. NumPy secara otomatis melakukan penjumlahan elemen-elemen matriks yang sesuai.

# cetak hasil
print("Hasil Penjumlahan Matriks dari NumPy") # Mencetak string "Hasil Penjumlahan Matriks dari NumPy"
print(result) # Mencetak hasil penjumlahan matriks X dan Y.
