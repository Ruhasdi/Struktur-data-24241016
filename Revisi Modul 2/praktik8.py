# membuat array
arr = [1, 2, 3, 4, 5] # Membuat array arr dengan 5 elemen: 1, 2, 3, 4, dan 5.

# mendeklarasikan nilai awal
start = 0 # Mendeklarasikan variabel start sebagai indeks awal untuk iterasi. start akan bernilai 0, yang merupakan indeks pertama dari array arr.
end = len(arr) - 1 # Mendeklarasikan variabel end sebagai indeks akhir untuk iterasi. len(arr) akan mengembalikan panjang array arr, yaitu 5.
# len(arr) - 1 akan mengembalikan indeks terakhir dari array arr, yaitu 4.

print("Reverse Traversal using while loop: ", end=" ") # Mencetak string "Reverse Traversal using while loop: " dan tidak memulai baris baru setelah mencetak string tersebut.
# Reverse Traversal dengan while
while start < end: # Melakukan iterasi menggunakan while loop selama start kurang dari end. Iterasi akan berhenti ketika start mencapai atau melebihi nilai end.

    arr[start], arr[end] = arr[end], arr[start] # Menukar nilai elemen pada indeks start dengan nilai elemen pada indeks end. Ini akan membalik urutan elemen-elemen array secara bertahap.
    start += 1 # Meningkatkan nilai start sebesar 1 setiap kali iterasi. Ini akan membuat iterasi maju ke indeks berikutnya dalam array.
    end -= 1 # Mengurangi nilai end sebesar 1 setiap kali iterasi. Ini akan membuat iterasi mundur ke indeks sebelumnya dalam array.

print(arr) # Mencetak array arr setelah iterasi selesai. Array arr akan dibalik urutannya.
