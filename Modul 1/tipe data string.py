a = 'Halo'
b = "Python"
c = """Ini adalah
string multi-baris"""
print(type(a))  # <class 'str'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'str'>

# indexing dan slicing 
text = "Python"
print(text[0])     # Output: P
print(text[-1])    # Output: n
print(text[0:3])   # Output: Pyt
print(text[:4])    # Output: Pyth
print(text[::2])   # Output: Pto (loncat 2 karakter)

# Operasi penggabungan string
print('Hello ' + 'World')

# Operasi pengulangan string
print('Hi' * 3)

# Operasi Pengecekan string
print('a' in 'data') # menghasilkan boolean (True/False)

# Operasi panjang string
print(len('Python'))

s = "python programming"
print(s.upper())       # 'PYTHON PROGRAMMING'
print(s.capitalize())  # 'Python programming'
print(s.title())       # 'Python Programming'
print(s.replace("python", "java"))  # 'java programming'
print(s.split())       # ['python', 'programming']
print(s.find("gram"))  # 10

# String format menggunakan F-String
name = "Adam"
age = 25
print(f"Halo, nama saya {name}, umur saya {age}")

# String format dengan format method
print("Halo, nama saya {}, umur saya {}".format(name, age))

