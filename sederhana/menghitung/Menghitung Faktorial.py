# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 15 Desember 2024
# Program Menghitung Faktorial

print("*"*40)
print("Menghitung Faktorial")
print("*"*40)

n = int(input("Masukkan bilangan: "))

faktorial = 1
for i in range(1,n + 1):
    faktorial *= i
    
print(f"faktorial dari {n} adalah {faktorial}.")