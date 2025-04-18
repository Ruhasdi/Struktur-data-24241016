# PERULANGAN-(LOOP)

# For-loop
# For kondisi
# Aksi

a = 0
a += 1 # a = a + 1
print(a)
a += 1
print(a)
a += 1
print(a)

# Perulangan dengan list
angka_list = [0,1,4,8,10]
for i in angka_list:
    print(f"i sekarang -> {i}")

print("ini angka akhir for 1 \n")

# Perulangan dengan range
angka_range = range(5) # diulang 5 kali

for i in angka_range:
    print(f"i sekarang -> {i} ")


    print("ini angka akhir for 2 \n")

    angka_range2 = range(1, 10) # diulang 9/10
    for i in angka_range2:
        print(f"i sekarang -> {i} ")
    print("ini akhir for 3 /n")
 

    # Perulangan dengan range
   
    angka_string = string= "dikta"  
    for i in angka_string:
        print(f"i sekarang -> {i}") 

print("akhir perulangan str/n")