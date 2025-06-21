# membuat array
arr = [1, 2, 3, 4, 5] # Membuat array arr dengan 5 elemen: 1, 2, 3, 4, dan 5.

# mendeklarasikan nilai awal
n = len(arr) # Mendapatkan panjang array arr dan menyimpannya dalam variabel n. n akan bernilai 5 karena array arr memiliki 5 elemen.
i = 0 # Mendeklarasikan variabel i sebagai indeks awal untuk iterasi. i akan bernilai 0, yang merupakan indeks pertama dari array arr.

print("Linear Traversal using while loop: ", end=" ") # Mencetak string "Linear Traversal using while loop: " dan tidak memulai baris baru setelah mencetak string tersebut.
# Linear Traversal dengan while
while i < n: # Melakukan iterasi menggunakan while loop selama i kurang dari n.Iterasi akan berhenti ketika i mencapai nilai n.
    print(arr[i], end=" ") # Mencetak nilai elemen yang sedang diakses dalam iterasi, dan tidak memulai baris baru setelah mencetak nilai tersebut.
# Elemen-elemen array akan dicetak secara berurutan, dipisahkan oleh spasi.
    i += 1 # Meningkatkan nilai i sebesar 1 setiap kali iterasi. Ini akan membuat iterasi maju ke indeks berikutnya dalam array.

print() 