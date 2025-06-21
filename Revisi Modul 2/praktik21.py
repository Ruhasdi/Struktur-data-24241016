import numpy as np

# vektor baris
vek_1 = np.array([1, 2, 3])

# vektor kolom
vek_2 = np.array([[1], 
                  [2],
                  [3]])

# atau menggunakan transpose()
vek_3 = np.array([1, 2, 3]).reshape(-1, 1)  # Menggunakan reshape untuk membuat vektor kolom

print("Vektor Baris")
print(vek_1)
print("Vektor Kolom")
print(vek_2)
print("Vektor Kolom dengan reshape()")
print(vek_3)