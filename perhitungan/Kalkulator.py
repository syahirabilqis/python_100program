# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  25 Oktober 2024
# Program Kalkulator Sederhana

print("*"*40)
print("Kalkulator Sederhana")
print("*"*40)


angka_1 =  float(input("Masukan angka 1 : "))
operator = input("operator (+,-,*,/) : ")
angka_2 = float(input("Masukan angka 2: "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil =  angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else:
    print("Operator tidak valid. Gunakan (+,-,*,/)")