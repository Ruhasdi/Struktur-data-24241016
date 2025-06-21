# Program penjumlahan matriks yang dibuat dari list

X = [[12,7,3],
    [4,5,6],
    [7,8,9]]
# Membuat matriks X dengan ukuran 3x3 dan elemen-elemen yang ditentukan.
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
# Membuat matriks Y dengan ukuran 3x3 dan elemen-elemen yang ditentukan.
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# Membuat matriks result dengan ukuran 3x3 dan elemen-elemen yang diinisialisasi dengan nilai 0.

# proses penjumlahan dua matriks menggunakan nested loop
# mengulang sebanyak row (baris)
for i in range(len(X)): # Mengulang sebanyak baris (row) matriks X. len(X) mengembalikan jumlah baris matriks X, yaitu 3.
   # mengulang sebanyak column (kolom)
   for j in range(len(X[0])): # Mengulang sebanyak kolom (column) matriks X. len(X[0]) mengembalikan jumlah kolom matriks X, yaitu 3.
       result[i][j] = X[i][j] + Y[i][j] # Menjumlahkan elemen-elemen matriks X dan Y pada posisi yang sama (i, j). Hasil penjumlahan disimpan dalam matriks result pada posisi yang sama (i, j).
print("Hasil Penjumlahan Matriks dari LIST") # Mencetak string "Hasil Penjumlahan Matriks dari LIST".

# cetak hasil penjumlahan secara iteratif
for r in result: # Mengulang sebanyak baris matriks result.
   print(r) # Mencetak setiap baris matriks result.