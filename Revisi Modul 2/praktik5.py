# membuat array
arr = [1, 2, 3, 4, 5] # - Membuat array arr dengan 5 elemen: 1, 2, 3, 4, dan 5.

# Reverse Traversal dari elemen akhir 
print("Reverse Traversal: ", end="") # Mencetak string "Reverse Traversal: " dan tidak memulai baris baru setelah mencetak string tersebut.
for i in range(len(arr) - 1, -1, -1): # - Melakukan iterasi pada indeks array arr secara terbalik, yaitu dari indeks terakhir hingga indeks pertama.
# len(arr) - 1 adalah indeks terakhir dari array arr.
# -1 adalah indeks sebelum indeks pertama (artinya iterasi akan berhenti ketika mencapai indeks 0).
#-1 sebagai step artinya iterasi akan mundur satu indeks setiap kali.
    print(arr[i], end=" ") # Mencetak nilai elemen yang sedang diakses dalam iterasi, dan tidak memulai baris baru setelah mencetak nilai tersebut.
# Elemen-elemen array akan dicetak secara terbalik, dipisahkan oleh spasi.

print()