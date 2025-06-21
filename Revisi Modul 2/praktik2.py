# impor libaray numpy
import numpy as np

# membuat array dengan numpy
nilai_siswa_1 = np.array([75, 65, 45, 80]) # Membuat array 1 dimensi dengan 4 elemen. Array ini memiliki bentuk (4,) yang berarti memiliki 4 elemen dalam 1 dimensi.
nilai_siswa_2 = np.array([[85, 55, 40], [50, 40, 99]]) # Membuat array 2 dimensi dengan 2 baris dan 3 kolom.
# Array ini memiliki bentuk (2,3) yang berarti memiliki 2 baris dan 3 kolom.

# cara akses elemen array
print(nilai_siswa_1[0]) # Mencetak nilai elemen pertama dari array nilai_siswa_1. Output: 75
print(nilai_siswa_2[1][1]) # Mencetak nilai elemen pada baris ke-2 dan kolom ke-2 dari array nilai_siswa_2. Output: 40

# mengubah nilai elemen array
nilai_siswa_1[0] = 88 # Mengubah nilai elemen pertama dari array nilai_siswa_1 menjadi 88.
nilai_siswa_2[1][1] = 70 # Mengubah nilai elemen pada baris ke-2 dan kolom ke-2 dari array nilai_siswa_2 menjadi 70.

# cek perubahannya dengan akses elemen array
print(nilai_siswa_1[0]) # Mencetak nilai elemen pertama dari array nilai_siswa_1 setelah diubah. Output: 88
print(nilai_siswa_2[1][1]) # Mencetak nilai elemen pada baris ke-2 dan kolom ke-2 dari array nilai_siswa_2 setelah diubah. Output: 70

# Cek ukuran dan dimensi array
print("Ukuran Array : ", nilai_siswa_1.shape) # Mencetak ukuran array nilai_siswa_1. Output: (4,)
print("Ukuran Array : ", nilai_siswa_2.shape) # Mencetak ukuran array nilai_siswa_2. Output: (2, 3)
print("Dimensi Array : ", nilai_siswa_2.ndim) # Mencetak dimensi array nilai_siswa_2. Output: 2